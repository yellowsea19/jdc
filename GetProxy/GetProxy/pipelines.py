# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from meitu.items import GetproxyItem
from GetProxy.MyLog import MyLogs
class GetproxyPipeline:

    def __init__(self):
        self.log=MyLogs()
    def process_item(self, item, spider):


        http='%s:%s'%(item['ip'],item['port'])
        self.log.info('********************1')
        with open('result.json','a+',encoding='utf-8') as f:
                f.write(item['ip']+':'+item['port'])
                f.write('\n')
                f.close()
        return item
