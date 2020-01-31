# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from redis_Spier_Pro.items import RedisSpierProItem
'''
一.修改爬虫文件
    1.导入scrapy-redis模块:from scrapy_redis.spiders import RedisSpider
    2.将当前爬虫类的父类修改成RedisSpider
    3.将allowed_domains和start_urls进行删除
    4.添加一个新的属性redis_key = 'xxx',该属性值表示的就是可以被共享的调度器队列的名称
二.进行配置文件的配置
    1.保证爬虫文件发起的请求都会被提交到可以被共享的调度器的队列中
        SCHEDULER = "scrapy_redis.scheduler.Scheduler"
    2.保证爬虫文件提交的item会被存储到可以被共享的管道中
    ITEM_PIPELINES = {
     'scrapy_redis.pipelines.RedisPipeline': 400
    }
    3.配置最终数据存储的redis数据库
        REDIS_HOST = 'redis服务的ip地址'
        REDIS_PORT = 6379
        REDIS_ENCODING = ‘utf-8’
        REDIS_PARAMS = {‘password’:’123456’}
    4.redis数据库的配置文件进行配置:关闭保护模式和注释掉bind 127.0.0.1
    5.开启redis服务和客户端
    6.执行爬虫文件:scrapy runspider xxx.py
    
'''
class RedisdemoSpider(RedisSpider):
    url = 'http://db.pharmcube.com/database/cfda/detail/cfda_cn_instrument/%d'
    page = 1
    name = 'redisDemo'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'cmda'
    
    
    def parse(self, response):
        
        
        if self.page < 130000:
            self.page += 1
            new_url = format(self.url%self.page)
			print(self.page)
            yield scrapy.Request(url=new_url,callback=self.parse)
            
        
        
        
