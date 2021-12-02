import scrapy


class FeedbackScraperItem(scrapy.Item):
    username = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    post_date = scrapy.Field()
