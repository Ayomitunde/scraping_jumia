# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def clean_data(value):
    chars_to_remove = ["out", "of"]
    for char in chars_to_remove:
        if char in value:
            value = value.replace(char, "")
    return value.strip()


class JumiaItem(scrapy.Item):
    name = scrapy.Field(input_processor = MapCompose(remove_tags, clean_data), output_processor = TakeFirst(),)
    price = scrapy.Field(input_processor = MapCompose(remove_tags, clean_data), output_processor = TakeFirst(),)
    rating= scrapy.Field(input_processor = MapCompose(remove_tags, clean_data), output_processor = TakeFirst(),)
    link = scrapy.Field(input_processor = MapCompose(remove_tags, clean_data), output_processor = TakeFirst(),)
    pass
