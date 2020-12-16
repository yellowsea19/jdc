# import requests
#
# res=requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=120734&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
# print(res.json())
# proxies={
#     'http': '%s:%s'%(res.json()['data'][0]['ip'],res.json()['data'][0]['port']),
#     'https': '%s:%s'%(res.json()['data'][0]['ip'],res.json()['data'][0]['port'])
# }
# res=requests.get(url='https://www.baidu.com',proxies=proxies)
# requests.encode='utf-8'
# print(res.text)