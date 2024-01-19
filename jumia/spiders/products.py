import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import JumiaItem
from scrapy.loader import ItemLoader


class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/mlp-clearance-sale/"]

    rules = (
        Rule(LinkExtractor(allow=(r"page=",))),
             Rule(LinkExtractor(allow=(r"#catalog-listing")), callback = "parse_items"),
        )

    def parse_items(self, response):
            l = ItemLoader(item = JumiaItem(), response=response)

            l.add_css("name", "h3.name")
            l.add_css("price", "div.prc")
            l.add_css("rating", "div.stars._s")
            l.add_css("link", "a.core::attr(href)")

            products =  response.css("article.prd._fb.col.c-prd")
            for items in products:
                 return l.load_item()

