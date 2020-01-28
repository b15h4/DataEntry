# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BcassessmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    PID = scrapy.Field()
    Address = scrapy.Field()
    Description = scrapy.Field()
    Bedrooms = scrapy.Field()
    Bathrooms = scrapy.Field()
    Carports = scrapy.Field()
    Garages = scrapy.Field()
    Land_Size = scrapy.Field()
    First_Flor_Area = scrapy.Field()
    Second_Flor_Area = scrapy.Field()
    Basement_Finish_Area = scrapy.Field()
    Strata_Area = scrapy.Field()
    Building_Storeys = scrapy.Field()
    Gross_Leasable_Area = scrapy.Field()
    Net_Leasable_Area = scrapy.Field()
    No_Of_Apartament_Units = scrapy.Field()
    Sold_Date = scrapy.Field()
    Sold_Price = scrapy.Field()
    
    Total_Value = scrapy.Field()
    Land = scrapy.Field()
    Buildings = scrapy.Field()
    Previous_Year_Value = scrapy.Field()
    Previous_Land = scrapy.Field()
    Previous_Buildings = scrapy.Field()
    Year_Built = scrapy.Field()
    Area_Jurisdiction_Roll = scrapy.Field()
    Legal_Description_and_Parcel_ID = scrapy.Field()