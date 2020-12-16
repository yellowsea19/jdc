import scrapy
from GetProxy.MyLog import MyLogs
from GetProxy.items import GetproxyItem
import requests
class GetproxySpider(scrapy.Spider):
    name = 'getProxy'
    # allowed_domains = ['taiyanghttp.com/free']
    start_urls = ['http://icanhazip.com/']

    def __init__(self):
        self.log=MyLogs()
    def parse(self, response):
        self.log.info(response.text)
        print(response.text)
        items=[]
        response.encode='utf-8'
        # # self.log.info(response.text)
        ip=response.xpath('//tr/td[1]/text()').extract()
        port=response.xpath('//tr/td[2]/text()').extract()
        for i in range(len(ip)):
            item=GetproxyItem()
            item['ip']=ip[i]
            item['port']=port[i]
            items.append(item)

        return items
        # self.log.info(ip)
        # self.log.info(port)
        # self.log.info(dict(zip(ip,port)))