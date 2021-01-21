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
        self.base_url='https://dev.yaoqianshu.co'


    def test_smscode(self,phone='13418914292',use='login',invite_code='V9K142'):
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

    def test_login(self,phone='12900200001',use='login'):
        '''登录'''
        uri='/v1/passport/login?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        #获取图形验证码
        # captcha_key,captcha_code=self.test_get_captcha()
        #发送短信验证码
        self.test_smscode(phone,use)
        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()

        headers={"content-type": "application/json; charset=utf-8",

                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,
                 }
        data={"type":"mobile_code",
              "account":phone,
              "password_or_code":"666666",
              "region_code":"86",
              "captcha_code":""
              }
        res=self.client.post(url=url,data=json.dumps(data),headers=headers,name='login')
        print('登录:'+str(phone))
        print(url)
        # print(json.dumps(data,sort_keys=True,indent=4))
        # print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))
        print(res.text)
        return res.json()

    def test_signin(self,access_token):
        '''任务-签到-签到动作'''
        uri='/v1/task/signin?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        # headers=self.headers
        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()

        headers={"content-type": "application/json; charset=utf-8",

                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,

                 }

        headers['Authorization']='Bearer '+access_token
        # headers={
        #     "content-type": "application/json; charset=utf-8",
        #      "Authorization":'Bearer '+access_token
        # }
        res=self.client.post(url=url,headers=headers,name='signin')
        print(res.status_code)
        print(res.text)

        print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))
        return res.json()

    @task
    def signs(self):
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

        login_info=self.test_login(phone=phone)
        access_token=login_info['payload']['access_token']
        r=self.test_signin(access_token)

        # res=self.test_treasure_box(login_info=r,phone=phone)
        # self.user.user_data_queue.put_nowait(phone)  # 把取出来的数据重新加入队列

        assert r['code'] == 0
        # assert res == 0
        # if r.status_code == 200:
        #     r.success()


class WebsiteUser(HttpUser):
    host = 'https://dev.yaoqianshu.co'
    tasks  = [UserBehavior]
    user_data_queue = queue.Queue()  # 创建队列，先进先出
    srart_index=12900004335
    for phone in range(srart_index,srart_index+6000):
        # data = {
        #     "phone": "%s" % index,
        # }
        user_data_queue.put_nowait(phone)  # 循环加入队列<全部>,循环完，继续执行
    min_wait = 1000
    max_wait = 3000
