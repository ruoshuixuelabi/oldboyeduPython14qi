增量式爬虫:每次爬取网站中更新的数据.
定时爬虫:使用脚本在指定时间内进行一次数据(最新更新)的爬取.

爬取数据的流程:
    1.指定url
    2.根据指定的url发请求,获取页面数据
    3.持久化存储

案例:
实现增量式爬虫的方案:
    1.在发送请求之前,判断url之前是否爬取过
        a.将即将进行爬取的数据对应的url存储到redis的set中.
        
    2.根据爬取到的数据进行重复过滤,然后在进行持久化存储
        b.将爬取到的数据给其生成一个唯一的标识(可以将该标识作为mysql的列.可以将该标识存储到redis的set中)





    