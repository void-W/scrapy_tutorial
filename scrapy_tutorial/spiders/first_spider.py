import scrapy
from bs4 import BeautifulSoup as bs


class FirstSpiderSpider(scrapy.Spider):
    name = 'first_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baidu.com/s?q2=红棉小冰']

    def parse(self, response):
        soup = bs(response.text, 'lxml')
        for search_result in soup.find_all(class_='result c-container new-pmd'):
            yield search_result.find(class_='t').get_text()
