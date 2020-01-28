# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ApishopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ArticleNumber = scrapy.Field()
    expectedDeliveryDateFormatted = scrapy.Field()
    AvailableQty = scrapy.Field()
    quantityFormatted = scrapy.Field()
    inventoryCount = scrapy.Field()
    inventoryCountFormatted = scrapy.Field()
