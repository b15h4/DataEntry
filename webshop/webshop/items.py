# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebshopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()   
    Title = scrapy.Field()
    ArticleNumber = scrapy.Field()
    Price = scrapy.Field()
    SpecialPrice = scrapy.Field()
    MinimumQuantity = scrapy.Field()
    Images = scrapy.Field()
    Description = scrapy.Field()