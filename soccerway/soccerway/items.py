# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoccerwayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TeamA = scrapy.Field()
    TeamB = scrapy.Field()
    Score = scrapy.Field()