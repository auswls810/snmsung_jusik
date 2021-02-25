# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JusikItem(scrapy.Item):
    code = scrapy.Field()
    price = scrapy.Field()
    total = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()

