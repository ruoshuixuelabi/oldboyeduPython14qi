# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from moviePro.items import MovieproItem
from redis import Redis
class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567tv.tv/frim/index1.html']
    # 负责数据库的连接,返回一个连接对象
    conn = Redis(host='127.0.0.1', port=6380)
    rules = (
        #规则解析器只可以对连接提取器提取到的连接发送请求
        Rule(LinkExtractor(allow=r'/frim/index1-\d+\.html'), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        li_list = response.xpath('//li[@class="p1 m1"]')
        for li in li_list:
            detail_url = 'http://www.4567tv.tv'+li.xpath('./a/@href').extract_first()
            # print(detail_url)
            ex = self.conn.sadd('urls',detail_url)
            if ex == 1:
                yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    
    def parse_detail(self,response):
        item = MovieproItem()
        item['name'] = response.xpath('/html/body/metaname="robots"content="noarchive"/div[3]/div[1]/div[2]/dl/dt[1]/text()').extract_first()
        print(item['name'])
        yield item
        
