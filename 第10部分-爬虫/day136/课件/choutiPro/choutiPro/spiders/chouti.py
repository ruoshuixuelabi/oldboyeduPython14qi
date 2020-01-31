# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from choutiPro.items import ChoutiproItem
from scrapy_redis.spiders import RedisCrawlSpider
class ChoutiSpider(RedisCrawlSpider):
    name = 'chouti'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'chouti'
    rules = (
        Rule(LinkExtractor(allow=r'/r/scoff/hot/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath('//div[@id="content-list"]/div')
        for div in div_list:
            item = ChoutiproItem()
            item['title'] = div.xpath('.//div[@class="part1"]/a/text()').extract_first()
            item['author'] = div.xpath('.//div[@class="part2"]/a[4]/b/text()').extract_first()
            
            yield item
        
