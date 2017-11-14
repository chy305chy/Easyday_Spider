# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EastdaySpiderProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EastdayspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 频道名称：toutiao,shehui,guonei,guoji等
    channel_name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 发布日期
    date = scrapy.Field()
    # 新闻来源
    source = scrapy.Field()
    # 唯一标识key
    rowkey = scrapy.Field()
    # 阅读数
    # urlpv = scrapy.Field()
    # 缩略图，数组
    miniimg = scrapy.Field()
    # 详情url，与http://mini.eastday.com/mobile/拼接后使用
    url = scrapy.Field()
    # 缩略图数目
    miniimg_size = scrapy.Field()
    #新闻类型
    type = scrapy.Field()
    # 新闻摘要
    brief = scrapy.Field()
    pass