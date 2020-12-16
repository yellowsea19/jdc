# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from meitu.MyLog import MyLogs

class GetproxyItem(scrapy.Item):
    # define the fields for your item here like:
    # log=MyLogs()
    port = scrapy.Field()
    ip = scrapy.Field()
    # log.info(port)
