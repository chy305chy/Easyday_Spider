#!/usr/bin/python
# coding=utf-8
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time,json,pymysql,re
from items import EastdayspiderItem

class EastdaySpiderProjectPipeline(object):
    def process_item(self, item, spider):
        return item

class MySqlDBPipline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='12321',
            db='eastday_db',
            charset='utf8'
        )
        self.conn.encoding = 'utf8'
        self.cur = self.conn.cursor()
        self.cur.execute("set names utf8")

    def process_item(self, item, spider):
        if isinstance(item, EastdayspiderItem):
            # item["crawled_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            try:
                # for key in dict(item):
                #     pass
                #     item[key] = str(item[key]).replace("'", "\\\'")
                #     item[key] = str(item[key]).replace('"', '\\\"')
                sql = """insert into t_eastday values("{rowkey}","{title}","{brief}","{pub_date}","{news_source}","{miniimg}","{url}","{miniimg_size}","{type}")""".format(rowkey=item['rowkey'], title=item['title'], brief=item['brief'], pub_date=item['date'], news_source=item['source'], miniimg=item['miniimg'], url=item['url'],miniimg_size=item['miniimg_size'], type=item['type'])

                sql2 = 'select 1 from t_eastday where url like "%s"' % item['url']
                print 'sql:', sql

                self.cur.execute(sql2)
                is_exist = self.cur.fetchone()
                if is_exist == (1,):
                    print '已存在%s' % item['url']
                else:
                    self.cur.execute(sql)
                    self.conn.commit()
                    print '插入成功'
            except Exception as e:
                print u'数据库error:', e
                pass
            else:
                print 'nonnonono'