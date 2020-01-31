# -*- coding: utf-8 -*-
import scrapy

#进行数据的爬取和解析
class FirstSpider(scrapy.Spider):
    #爬虫文件的名称:根据名称可以定位到指定的爬虫文件
    name = 'first'
    #允许的域名
    # allowed_domains = ['www.baidu.com']
    #起始url列表
    start_urls = ['https://www.sogou.com/']

    #用于解析:response就是起始url对应的响应对象
    def parse(self, response):
        print(response)

