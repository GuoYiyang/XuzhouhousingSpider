# -*- coding: utf-8 -*-
import scrapy
from XuzhouSpider.items import XuzhouspiderItem


class HousePositionSpider(scrapy.Spider):
    name = 'house_position'
    allowed_domains = ['xuzhou.ganji.com']
    start_urls = ['http://xuzhou.ganji.com/zufang/']

    def parse(self, response):
        for house in response.xpath('//div[@class="f-list-item ershoufang-list"]'):
            item=XuzhouspiderItem()
            item['name']=house.xpath('./dl/dd[@class="dd-item title"]/a/text()').extract()
            item['size']=house.xpath('./dl/dd[@class="dd-item size"]/span/text()').extract()
            item['address']=house.xpath('./dl/dd[@class="dd-item address"]/span/a/span/text()').extract()
            item['price']=house.xpath('./dl/dd[@class="dd-item info"]/div/span[@class="num"]/text()').extract()
            yield item
        new_links = response.xpath('//div[@class="pageBox"]/a[@class="next"]/@href').extract()
        if new_links and len(new_links)>0:
            new_link = new_links[0]
            yield scrapy.Request(new_link,callback=self.parse)

