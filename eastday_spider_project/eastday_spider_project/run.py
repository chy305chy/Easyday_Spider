# -*- coding: utf-8 -*-
from scrapy import cmdline
import redis, time, threading
from multiprocessing import Process

# cmd = 'scrapy crawl {0}'.format('eastdayspider')
# cmdline.execute(cmd.split())


start_urls = ['http://mini.eastday.com/',
#国内
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0010',
#国际
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0011',
#军事
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0005',
#社会
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0003',
#娱乐
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0002',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5064',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5065',
#健康
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0019',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5004',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5005',
#时尚
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0015',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5039',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5040',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5041',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5042',
#科技1
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0008',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5001',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5002',
#汽车
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0012',
#历史
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0018',
#游戏
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0007',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5079',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5080',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5081',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5082',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5090',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5092',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5093',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5083',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5084',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5087',
#星座
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0020',
#家居
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0021',
#英超
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5016',
#棋牌
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5017',
#体育
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0006',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5009',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5010',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5011',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5012',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5013',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5014',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5015',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5017',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5018',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5019',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5020',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5021',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5022',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5055',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5056',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5058',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5059',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5060',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5061',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5062',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5063',
#女性
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0009',
#新闻-头条
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0001',
#财经
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0004',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5024',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5025',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5026',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5027',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5028',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5029',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5030',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5032',
# 'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5034',
#财经-股市
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5031',
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5033',
#教育
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0013',
#房产
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0014',
#笑话
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0017',
#娱乐
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5037',
#娱乐-电影
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5035',
#娱乐-电视
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5036',
#娱乐-综艺
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=5038',
#自然
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0023',
#情感
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0024',
#旅游
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0025',
#猎奇
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0026',
#宠物
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0028',
#动漫
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0029',
#育儿
'http://ttpc.dftoutiao.com/jsonpc/refresh?type=0030',
]

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

def check_redis_requests():
    while(1):
        for url in start_urls:
            r.sadd('eastday_spider_project:start_urls', url)
            # print u'插入到start_urls的:',r.smembers('eastdayspider:start_urls')

        count = 0
        while(count < 30):
            if r.exists('eastday_spider_project:repquests'):
                time.sleep(60)
                count = 0
            else:
                count += 1
                time.sleep(10)

def run_spider():
    cmdline.execute("scrapy crawl eastday_spider".split())

if __name__ == '__main__':
    pass

p1 = Process(target=check_redis_requests)
p2 = Process(target=run_spider)

p1.start()
time.sleep(5)
p2.start()

p1.join()
p2.join()