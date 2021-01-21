from locust import TaskSet, task, HttpUser
import queue
import os
import requests
import json,time
import hmac
import time
requests.packages.urllib3.disable_warnings()
class UserBehavior(TaskSet):

    def on_start(self):
        self.base_url='https://api01.yaoqianshu.co'


    def test_smscode(self,phone='13418914292',use='register',invite_code='V9K142'):
        '''获取短信验证码 用户登录/找回密码/注册短信'''
        uri='/v1/passport/smscode?use=%s&region_code=86&mobile=%s&invite_code=%s&tid=o2rze1pr9dvp8k5934'%(use,phone,invite_code)
        url=self.base_url+uri
        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()

        headers={"content-type": "application/json; charset=utf-8",

                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,

                 }
        res=self.client.get(url=url,headers=headers,verify=False,name='smscode')
        print('smscode'+str(phone))
        # print(url)
        # print(json.dumps(res.json(),ensure_ascii=False))

    def test_register(self,phone='12900209912',invite_code='V9K142'):
        '''注册流程'''
        #发送短信验证码
        # self.test_smscode(captcha_key,captcha_code,phone)
        self.test_smscode(phone=phone,invite_code=invite_code)
        #注册
        uri='/v1/passport/register?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        data={
            "register_type":"mobile_code",
            "mobile":phone,
            "code":666666,
            "invite_code":invite_code
        }

        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()

        headers={"content-type": "application/json; charset=utf-8",

                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,

                 }
        res=self.client.post(url=url,data=json.dumps(data),verify=False,headers=headers,name='register')
        res.encoding='utf-8'
        print('register：'+str(phone))
        print(url)
        # print(json.dumps(data,sort_keys=True,indent=4))
        print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))
        return res.json()
    def test_treasure_box(self,login_info,phone='12900200011'):
        '''做宝箱任务'''
        uri='/v1/task/treasure_box?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        login_info=login_info
        import time
        # h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%str(int(time.time())), digestmod='sha256')

        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()
        # print(h_str)
        headers={"content-type": "application/json; charset=utf-8",
                 "Authorization":'Bearer '+login_info['payload']['access_token'],
                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,

                 }
        res=self.client.post(url=url,headers=headers,name='treasure_box')
        print('宝箱任务'+str(phone))
        print(url)
        # print(headers)
        print(res.text)

    @task
    def register(self):
        try:
            # get_nowait() 取不到数据直接崩溃；get() 取不到数据会一直等待
            phone = self.user.user_data_queue.get_nowait()  # 取值顺序 'username': 'test0000'、'username': 'test0001'、'username': 'test0002'...
        except queue.Empty:  # 取不到数据时，走这里
            print('account data run out, test ended.')
            exit(0)
        print('register with user: {}'.format(''))
        # payload = {
        #     'username': data['username'],
        #     'password': data['password']
        # }
        # r = self.client.post('/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F', data=payload)

        r=self.test_register(phone)
        self.test_treasure_box(login_info=r,)
        # res=self.test_treasure_box(login_info=r,phone=phone)
        # self.user.user_data_queue.put_nowait(phone)  # 把取出来的数据重新加入队列

        assert r['code'] == 0
        # assert res == 0
        # if r.status_code == 200:
        #     r.success()

class WebsiteUser(HttpUser):
    host = 'https://api01.yaoqianshu.co'
    tasks  = [UserBehavior]
    user_data_queue = queue.Queue()  # 创建队列，先进先出
    srart_index=12900207331
    for phone in range(srart_index,srart_index+20):
        # data = {
        #     "phone": "%s" % index,
        # }
        user_data_queue.put_nowait(phone)  # 循环加入队列<全部>,循环完，继续执行
    min_wait = 1000
    max_wait = 3000
