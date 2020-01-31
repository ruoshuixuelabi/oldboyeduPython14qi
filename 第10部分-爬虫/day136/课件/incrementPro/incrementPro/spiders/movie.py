# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from redis import Redis
from incrementPro.items import IncrementproItem
class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567tv.tv/frim/index7-11.html']

    rules = (
        Rule(LinkExtractor(allow=r'/frim/index7-\d+\.html'), callback='parse_item', follow=True),
    )
    #创建redis链接对象
    conn = Redis(host='127.0.0.1',port=6380)
    
    def parse_item(self, response):
        li_list = response.xpath('//li[@class="p1 m1"]')
        for li in li_list:
            #获取详情页的url
            detail_url = 'http://www.4567tv.tv'+li.xpath('./a/@href').extract_first()
            #将详情页的url存入redis的set中
            ex = self.conn.sadd('urls',detail_url)
            if ex == 1:
                print('该url没有被爬取过，可以进行数据的爬取')
                yield scrapy.Request(url=detail_url,callback=self.parst_detail)
            else:
                print('数据还没有更新，暂无新数据可爬取！')

    #解析详情页中的电影名称和类型，进行持久化存储
    def parst_detail(self,response):
        item = IncrementproItem()
        item['name'] = response.xpath('//dt[@class="name"]/text()').extract_first()
        item['kind'] = response.xpath('//div[@class="ct-c"]/dl/dt[4]//text()').extract()
        item['kind'] = ''.join(item['kind'])
        yield item