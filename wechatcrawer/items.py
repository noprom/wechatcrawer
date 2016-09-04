# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WechatcrawerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WechatArticle(scrapy.Item):
    '''
    微信公众号文章实体
    '''
    title = scrapy.Field()
    key = scrapy.Field()
    is_head = scrapy.Field()
    url = scrapy.Field()
    create_time = scrapy.Field()
    biz = scrapy.Field()
    mid = scrapy.Field()
    idx = scrapy.Field()
    sn = scrapy.Field()