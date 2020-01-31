# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from incrementByDataPro.items import IncrementbydataproItem
from redis import Redis
import hashlib
class QiubaiSpider(CrawlSpider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    rules = (
        Rule(LinkExtractor(allow=r'/text/page/\d+/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/text/$'), callback='parse_item', follow=True),
    )
    #创建redis链接对象
    conn = Redis(host='127.0.0.1',port=6380)
    
    def parse_item(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')

        for div in div_list:
            item = IncrementbydataproItem()
            item['author'] = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span[2]/h2/text()').extract_first()
            item['content'] = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            #将解析到的数据值生成一个唯一的标识进行redis存储
            source = item['author']+item['content']
            source_id = hashlib.sha256(source.encode()).hexdigest()
            #将解析内容的唯一表示存储到redis的data_id中
            ex = self.conn.sadd('data_id',source_id)

            if ex == 1:
                print('该条数据没有爬取过，可以爬取......')
                yield item
            else:
                print('该条数据已经爬取过了，不需要再次爬取了!!!')



