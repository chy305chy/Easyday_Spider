#!/usr/bin/python
# coding=utf-8
# -*- coding: utf-8 -*-
import json
from scrapy_redis.spiders import RedisSpider
from eastday_spider_project.items import EastdayspiderItem

class EasydaySpider(RedisSpider):
    name = 'eastday_spider'
    redis_key = 'eastday_spider_project:start_urls'

    def parse(self, response):
        item = EastdayspiderItem()
        # 解析response
        res_body = response.body
        res1 = res_body.split('null(')[1]
        res2 = res1[0:len(res1)-1]
        newsListJson = json.loads(res2)
        for dict in newsListJson['data']:
            item['title'] = dict['topic'].encode('utf8').strip()
            item['date'] = dict['date'].encode('utf8').strip()
            item['source'] = dict['source'].encode('utf8').strip()
            item['rowkey'] = dict['rowkey'].encode('utf8').strip()
            item['miniimg'] = dict['miniimg']
            item['url'] = dict['url'].encode('utf8').strip()
            item['miniimg_size'] = dict['miniimg_size'].encode('utf8').strip()
            item['brief'] = dict['brief'].encode('utf8').strip()
            item['type'] = dict['type'].encode('utf8').strip()
            yield item