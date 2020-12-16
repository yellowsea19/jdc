# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from GetProxy.User_Agent_switch import choose_agent
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import scrapy
from scrapy import signals
import random,requests,time

class ProxyMiddleware(object):

    def __init__(self):
        self.proxy=self.get_proxy()

    def get_proxy(self):
        res=requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=120734&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
        print(res.json())
        if res.json()['code'] !=0:
            time.sleep(2)
            self.get_proxy()
        else:
            ip=res.json()['data'][0]['ip']
            port=res.json()['data'][0]['port']
            return 'http://%s:%s'%(ip,port)

    def process_request(self, request, spider):
        # res=requests.get('http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=120734&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
        # print(res.json())
        # if res.json()['code'] !=0:
        #     self.process_request(self, request, spider)

        # ip = self.proxy['data'][0]['ip']
        # port = self.proxy['data'][0]['port']
        # proxy={
        #     'http':'http://%s:%s'%(ip,port),
        #     # 'https':'//%s:%s'%(ip,port),
        #
        # }
        # print(proxy)
        request.meta['proxy'] = self.get_proxy()
        return None

    def process_exception(self, request, exception, spider):
        ## 针对超时和无响应的reponse,获取新的IP,设置到request中，然后重新发起请求
        if '10061' in str(exception) or '10060' in str(exception):
            # new_ip = self.get_proxy()

        # if new_ip:

            request.meta['proxy'] = self.get_proxy()

        # if isinstance(exception, self.EXCEPTIONS_TO_RETRY) and not request.meta.get('dont_retry', False):
        #     return self._retry(request, exception, spider)

class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):

        request.headers.setdefault('User-Agent', choose_agent())

class GetproxySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GetproxyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
