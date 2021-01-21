import unittest
import requests
import json
import re
import warnings
import pymysql
import hmac
import time
warnings.filterwarnings("ignore")
class yqs(unittest.TestCase):

    def setUp(self):
        self.base_url='https://dev.yaoqianshu.co'
        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()

        self.headers={"content-type": "application/json; charset=utf-8",

                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,

                 }
        # self.headers={
        #     "Content-Type":"application/x-www-form-urlencoded",
        #     # "timezone":"Asia/Shanghai"
        # }
        # self.phone='13418914292'
        # self.access_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvZGV2Lnlxcy55YW94aW4uY29cL3YxXC9wYXNzcG9ydFwvbG9naW4iLCJpYXQiOjE2MDYyODM2OTAsImV4cCI6MTYwNjI4NzI5MCwibmJmIjoxNjA2MjgzNjkwLCJqdGkiOiIxR3dkT1VxdVJhTWNCQkNpIiwic3ViIjoiTVhYUDM2IiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.scMWLblxSZTNKSXXJof9Cl4PvGLpP_0Ka4WYlCoUcmU'

    def test_get_captcha(self):
        '''获取图形验证码'''

        uri='/v1/passport/captcha?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        # data={
        #     "captcha_code":1
        # }
        res=requests.get(url=url,headers=self.headers,verify=False)
        print('获取图形验证码')
        print(url)
        # print(res.json())
        print(res.text)
        result=res.json()
        # print(json.dumps(result,sort_keys=True, indent=4))
        return result['payload']['key'],result['payload']['captcha_code']
    def test_smscode(self,phone='12900200003',use='login',invite_code='V9K142'):
        '''获取短信验证码 用户登录/找回密码/注册短信'''
        uri='/v1/passport/smscode?use=%s&region_code=86&mobile=%s&invite_code=%s&tid=o2rze1pr9dvp8k5934'%(use,phone,invite_code)
        url=self.base_url+uri
        print(url)
        h = hmac.new(b"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840", msg=b"1.0.21,%s,ios,aaeb3ed1-04f3-42f7-a475-6e3e4a94e840"%bytes(str(int(time.time())), encoding='utf-8'), digestmod='sha256')

        h_str = h.hexdigest()

        headers={"content-type": "application/json; charset=utf-8",

                 "signkey":"aaeb3ed1-04f3-42f7-a475-6e3e4a94e840",
                 "version":"1.0.21",
                 "timestamp":str(int(time.time())),
                 "device-type":"ios",
                 "sign":h_str,

                 }
        res=requests.get(url=url,headers=headers,verify=False)
        print(res.request.url)
        print('smscode'+str(phone))
        # print(json)
        # print(url)
        print(json.dumps(res.json(),ensure_ascii=False))

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
        res=requests.post(url=url,data=json.dumps(data),headers=headers)
        print('登录:'+str(phone))
        print(url)
        # print(json.dumps(data,sort_keys=True,indent=4))
        # print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))
        print(res.text)
        return res.json()

    def test_treasure_box(self,phone='12900200011'):
        '''做宝箱任务'''
        uri='/v1/task/treasure_box?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        login_info=self.test_login(phone)
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
        res=requests.post(url=url,headers=headers)
        print('宝箱任务'+str(phone))
        print(url)
        # print(headers)
        print(res.text)
        # print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))



    def test_task_list(self,phone='12900200011'):
        '''任务-任务列表'''
        uri='/v1/task/list?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        login_info=self.test_login(phone)
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
        res=requests.get(url=url,headers=headers)
        print(res.text)
        print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))

    def test_signin_detail(self,access_token):
        '''任务-签到-签到详情'''
        uri='/v1/task/signin?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        headers={
            "content-type": "application/json; charset=utf-8",
             "Authorization":'Bearer '+access_token
        }
        res=requests.get(url=url,headers=headers)
        print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))

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
        res=requests.post(url=url,headers=headers)
        print(res.status_code)
        print(res.text)

        print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))


    def test_team_info(self,phone='12900200001'):
        '''我的团队 - 团队信息'''
        uri='/v1/team/info?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        login_info=self.test_login(phone)
        headers={"content-type": "application/json; charset=utf-8",
                 "Authorization":'Bearer '+login_info['payload']['access_token']}
        res=requests.get(url=url,headers=headers)

        print('我的团队 - 团队信息:'+str(phone))
        print(url)
        # print(json.dumps(headers,sort_keys=True,indent=4))
        # print(res.text)
        # # print(json.dumps(res.json(),ensure_ascii=False))
        # print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))
        # print(res.json()['payload']['my']['invite_code'])
        return res.json()['payload']['my']['invite_code']

    def test_apply_upgrade(self,phone='12900232901'):
        '''身份升级-申请升级'''
        uri='/v1/team/apply_upgrade?tid=o2rze1pr9dvp8k5934'
        url=self.base_url+uri
        login_info=self.test_login(phone)
        headers={"content-type": "application/x-www-form-urlencoded",
                 "Authorization":'Bearer '+login_info['payload']['access_token']}
        res=requests.post(url=url,headers=headers)
        print('身份升级-申请升级:'+str(phone))
        print(url)
        # print(json.dumps(headers,sort_keys=True,indent=4))
        # # print(res.text)
        # # print(json.dumps(res.json(),ensure_ascii=False))
        # print(json.dumps(res.json(),sort_keys=True,indent=4,ensure_ascii=False))


    def test_upgrade_admin(self,phone='12900232901'):
        #后台审核身份升级
        print('1-----------------------------------------------------')
        url='http://dev.yqs.yaoxin.co/pm/auth/login'
        res=requests.get(url=url,verify=False)
        Cookie=re.findall(r'XSRF-TOKEN=(.*?);',res.headers['Set-Cookie'])[0]
        session=re.findall(r'session=(.*?);',res.headers['Set-Cookie'])[0]
        token=re.findall(r'Dcat.token = "(.*?)"',res.text)[0]
        print('2------------------------------------------------------------')
        url='http://dev.yqs.yaoxin.co/pm/auth/login'
        headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Cookie":'XSRF-TOKEN='+Cookie+";_session="+session,
                 "X-CSRF-TOKEN": token,
                 "X-Requested-With": "XMLHttpRequest",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                 }

        data={
            "_token":token,
            "username":"admin",
            "password":"admin888",
        }
        res=requests.post(url=url,data=data,headers=headers,verify=False)
        self.assertEqual(True,res.json()['status'])
        # print(res.text)
        # print(res.headers)
        print('3--------------------------------------------------------')
        url='http://dev.yqs.yaoxin.co/pm'
        Cookie=re.findall(r'XSRF-TOKEN=(.*?);',res.headers['Set-Cookie'])[0]

        session=re.findall(r'session=(.*?);',res.headers['Set-Cookie'])[0]

        headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Cookie":'XSRF-TOKEN='+Cookie+";_session="+session,
                 "X-Requested-With": "XMLHttpRequest",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                 }
        # print(headers)
        res=requests.get(url=url,headers=headers)
        # print(res.text)
        # print(res.headers)
        # print(res.status_code)

        print('4-------------------------------------------------')
        url='http://dev.yqs.yaoxin.co/pm/dcat-api/value'
        Cookie=re.findall(r'XSRF-TOKEN=(.*?);',res.headers['Set-Cookie'])[0]

        session=re.findall(r'session=(.*?);',res.headers['Set-Cookie'])[0]

        token=re.findall(r'Dcat.token = "(.*?)"',res.text)[0]

        headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Cookie":'XSRF-TOKEN='+Cookie+";_session="+session,
                 "X-CSRF-TOKEN": token,
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                 }
        data='_key=App%5CTenant%5CMetrics%5CExamples%5CProductOrders'
        # print(headers)
        res=requests.post(url=url,data=data,headers=headers)
        # print(res.headers)
        # print(res.status_code)

        self.db=pymysql.connect(host ='47.106.227.43', port =3306, user = 'huanghai',passwd = 'admin888',db='api2_yqs_dev')
        cursor=self.db.cursor()
        sql="select id from user where mobile=%s "
        cursor.execute(sql,phone)
        result=cursor.fetchone()
        user_id=result[0]
        sql='select id from user_grade_log where user_id=%s order by id desc'

        cursor.execute(sql,user_id)
        result=cursor.fetchone()
        grade_id=result[0]
        print('5---------------------------------------------------')
        url='http://dev.yqs.yaoxin.co/pm/user_grade_log/{}/edit?apply_status=1&_pjax=%23pjax-container'.format(grade_id)
        Cookie=re.findall(r'XSRF-TOKEN=(.*?);',res.headers['Set-Cookie'])[0]

        session=re.findall(r'session=(.*?);',res.headers['Set-Cookie'])[0]
        # token=re.findall(r'Dcat.token = "(.*?)"',res.text)[0]
        headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Cookie":'XSRF-TOKEN='+Cookie+";_session="+session,
                 "X-CSRF-TOKEN": token,
                 "X-Requested-With": "XMLHttpRequest",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                 }
        res=requests.get(url=url,headers=headers)
        print(res.status_code)



        print('6-----------------------------------------------------------------------------------')
        url='http://dev.yqs.yaoxin.co/pm/user_grade_log/%s'%grade_id
        Cookie=re.findall(r'XSRF-TOKEN=(.*?);',res.headers['Set-Cookie'])[0]

        session=re.findall(r'session=(.*?);',res.headers['Set-Cookie'])[0]

        headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Cookie":'XSRF-TOKEN='+Cookie+";_session="+session,
                 "X-CSRF-TOKEN": token,
                 "X-Requested-With": "XMLHttpRequest",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                 }
        data={
        "apply_status_not_in":"1",
        "apply_status": 3,
        "created_at": 1607418991,
        "updated_at": 0,
        "remark":"aaaaaaa",
        "_method": "PUT",
        "_token": token,
        "_previous_": "https://dev.yqs.yaoxin.co/pm/user_grade_log?_selector%5Bapply_status%5D=3",
        }
        res=requests.post(url=url,data=data,headers=headers)

        # print(headers)
        # print(res.status_code)
        # print(res.json())
        print(url)
        return res.json()['data']['type']


    def test_huiyuan(self,start_phone=12900232246,invite_code='MXW443',nums=10):
        '''成为普通会员'''
        # start_phone=12900232151
        # self.test_register(start_phone)
        # invite_code=self.test_team_info(start_phone)
        for phone in range(start_phone+1,start_phone+1+nums):
            self.test_register(phone,invite_code)
            self.test_treasure_box(phone)
        self.test_apply_upgrade(start_phone)
        self.test_upgrade_admin(start_phone)

    def test_upgrade_daoshi(self,start_phone=12900232687,invite_code='MXW443'):
        '''成为导师'''
        # start_phone=12900232151
        #注册start_phone
        self.test_register(phone=start_phone,invite_code=invite_code)
        invite_code=self.test_team_info(start_phone)
        #先成为会员,下级15个用户
        self.test_huiyuan(start_phone,invite_code=invite_code,nums=15)
        #让下级15个用户都成为会员

        #获取下级15个用户邀请码
        next_phone=start_phone
        for phone in range(start_phone+1,start_phone+1+15):
            invite_code=self.test_team_info(phone)
            for phone in range(next_phone+16,next_phone+26):
                self.test_register(phone=phone,invite_code=invite_code)
                self.test_treasure_box(phone)
            next_phone+=10
        #下级15个用户申请成为会员
        for phone in range(start_phone+1,start_phone+1+15):
            self.test_apply_upgrade(phone)
            self.test_upgrade_admin(phone)
        #申请成为导师
        self.test_apply_upgrade(start_phone)
        self.test_upgrade_admin(start_phone)




    def test_upgrade_hehuoren(self,start_phone=12900232900):
        '''升级成为合伙人'''
        #注册20个导师
        for phone in range(start_phone,start_phone+3200,160):
            self.test_upgrade_daoshi(phone)







    def test_apply_upgrade_team(self):

        phone=12900230016
        for i in range(phone,phone+1):
            self.test_apply_upgrade(i)


    def test_signs(self):
        '''批量签到12900000267'''
        for phone in range(12900001547,12900019999):
            login_info=self.test_login(phone=phone)
            access_token=login_info['payload']['access_token']
            self.test_signin(access_token)














