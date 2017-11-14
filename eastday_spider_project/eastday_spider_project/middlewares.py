# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from scrapy import signals
from settings import PROXIES

# 随机使用预定义列表里的 User-Agent类
class UserAgentMiddleware(object):
    def __init__(self, agents):
        # 使用初始化的agents列表
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings的USER_AGENT列表并返回
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        # 随机设置Request报头header的User-Agent
        request.headers.setdefault('User-Agent', random.choice(self.agents))


# 随机使用预定义列表里的 Proxy代理
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 随机获取from settings import PROXIES里的代理
        proxy = random.choice(PROXIES)

        # 如果代理可用，则使用代理
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            # 对代理数据进行base64编码
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            # 添加到HTTP代理格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        else:
            print "****代理失效****" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']

class EastdaySpiderProjectSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
