# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TargetspiderItem(scrapy.Item):
    # define the fields for your item here like:
    ProductName = scrapy.Field()
    Brand = scrapy.Field()
    ProductLink = scrapy.Field()
    Path = scrapy.Field()
    Category = scrapy.Field()
    SubCategory = scrapy.Field()
    StarRating = scrapy.Field()
    Price = scrapy.Field()
    Details = scrapy.Field()
    DrugFacts = scrapy.Field()
    NumberofReviews = scrapy.Field()
