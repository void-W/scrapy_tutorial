import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = 'first_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
