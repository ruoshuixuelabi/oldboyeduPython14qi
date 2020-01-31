# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# class CrawldemoSpider(CrawlSpider):
#     name = 'crawlDemo'
#         # allowed_domains = ['www.xxx.com']
#     start_urls = ['https://dig.chouti.com/all/hot/recent/1']
#     # 连接提取器:前提(follow=False),作用就是用来提取起始url对应页面中符合要求的连接
#     link = LinkExtractor(allow=r'/all/hot/recent/\d+')
#     rules = (
#         # 规则解析器对象:将连接提取器提取到的连接对应的页面源码数据根据只用要求进行解析
#         #follow=True:让连接提取器继续作用在连接提取器提取出的来连接所对应的页面源码中
#         Rule(link, callback='parse_item', follow=True),
#     )
#
#     def parse_item(self, response):
#         print(response)

class CrawldemoSpider(CrawlSpider):
    name = 'crawlDemo'
        # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/pic/']
    # 连接提取器:前提(follow=False),作用就是用来提取起始url对应页面中符合要求的连接
    link = LinkExtractor(allow=r'/pic/page/\d+\?s')
    link1 = LinkExtractor(allow=r'/pic/$')
    rules = (
        # 规则解析器对象:将连接提取器提取到的连接对应的页面源码数据根据只用要求进行解析
        #follow=True:让连接提取器继续作用在连接提取器提取出的来连接所对应的页面源码中
        Rule(link, callback='parse_item', follow=True),
        Rule(link1, callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        print(response)
