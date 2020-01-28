# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirdrieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Plan = scrapy.Field()
    Block_Unit = scrapy.Field()
    Lot = scrapy.Field()
    Roll = scrapy.Field()
    Assessed_Value = scrapy.Field()
    Land_Use = scrapy.Field()
    Classifications = scrapy.Field()
    Parcel_Area = scrapy.Field()
    Year_Built = scrapy.Field()
    Living_Area_above_Grade = scrapy.Field()
    Building_Description = scrapy.Field()
    Finished_Area_Below_Grade = scrapy.Field()
    Garage = scrapy.Field()
    Deck_s = scrapy.Field()
    Veranda_s = scrapy.Field()
    Fireplace_s = scrapy.Field()
    Walkout_Basement = scrapy.Field()
