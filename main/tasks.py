from feedbackparser.celery import app


@app.task()
def crawl():
    from main.crawler import spider_crawl
    return spider_crawl()
