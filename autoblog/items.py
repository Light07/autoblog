# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoblogItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
    categories = scrapy.Field()
    contents = scrapy.Field()
    desc = scrapy.Field()
    url = scrapy.Field()
