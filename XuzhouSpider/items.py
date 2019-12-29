# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XuzhouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #楼盘名称
    name=scrapy.Field()
    #位置
    address=scrapy.Field()
    #价格
    price=scrapy.Field()
    #描述
    size=scrapy.Field()
