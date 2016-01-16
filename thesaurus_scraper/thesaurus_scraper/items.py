# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ThesaurusScraperItem(Item):
    relevance_3_words = Field()
    relevance_2_words = Field()
    relevance_1_words = Field() 
