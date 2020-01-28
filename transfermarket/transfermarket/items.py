# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TransfermarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    club_name = scrapy.Field()
    loan_players = scrapy.Field()
    average_loan_period_in_years = scrapy.Field()
    club_link_TFM = scrapy.Field()
    loan_players_link = scrapy.Field()
    filter_loan_type_TFM = scrapy.Field()
    filter_season_id_TFM = scrapy.Field()
    appearances = scrapy.Field()
    starting_formation= scrapy.Field()
    goals = scrapy.Field()
    average_minutes_played = scrapy.Field()
    loan_fee = scrapy.Field()
    market_value_at_start_of_loan = scrapy.Field()