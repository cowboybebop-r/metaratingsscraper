import json

import scrapy
from scrapy.spiders import CrawlSpider

from ..items import FeedbackScraperItem


class FeedbackSpider(scrapy.Spider):
    name = "feedbacks"
    start_urls = ["https://metaratings.ru/bookmakersrating/olimp/reviews/?page=page-1"]
    allowed_domains = ['metaratings.ru']
    page = 1

    def parse(self, response, **kwargs):
        item = FeedbackScraperItem()
        for feedback in response.css("div.sentiment-review-item"):
            item.update(
                {"username": feedback.css("div.sentiment-review-item-name::text").get(),
                 "source": feedback.css("span.sentiment-review-item-link::text").get(),
                 "content": feedback.css("div.sentiment-review-item-text::text").get(),
                 "post_date": feedback.css("div.sentiment-review-item-date::text").get()
                 }
            )
            yield item

