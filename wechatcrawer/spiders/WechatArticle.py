# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from wechatcrawer.items import WechatArticleItem


class WechatarticleSpider(scrapy.Spider):
    name = "WechatArticle"
    allowed_domains = ["http://mp.weixin.qq.com/"]
    start_urls = (
        'http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MzAwMjUxMzE5NQ==&uin=MTE0MjU2NDkyNA%3D%3D&key=7b81aac53bd2393d34cf300edca416d3dfd0cfc6e214cb2314e7f721f60e679e79394c0764b1824388156d109e5117c359e78563ce485b6c&devicetype=android-21&version=2603163c&lang=zh_CN&nettype=WIFI&ascene=3&pass_ticket=FGu256ABQsRL5PEPzsXDO1jiUh4cjpr0M5c0WwAF8RVfbzux1ZEgUtERhRf5iAvB&wx_header=1',
    )

    rules = [
        Rule(LinkExtractor(allow=("http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=([\w]+)$",)),
             callback='parse',
             follow=True),
    ]

    def parse(self, response):
        item = WechatArticleItem()
        print response.url
        yield item
