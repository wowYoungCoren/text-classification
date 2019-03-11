# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinesenewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    url = scrapy.Field() #新闻的url
    title = scrapy.Field()  # 新闻的标题
    content = scrapy.Field()  # 新闻的内容

