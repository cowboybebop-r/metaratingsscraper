import django
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

django.setup()


def spider_crawl():
    from feedbackscraper.feedbackscraper.spiders import FeedbackSpider
    settings = {
        'ITEM_PIPELINES': {
            'feedbackscraper.feedbackscraper.pipelines.FeedbackscraperPipeline': 300,
        }
    }
    process = CrawlerProcess(settings=settings)
    process.crawl(FeedbackSpider)
    process.start()
