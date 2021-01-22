import scrapy
from bs4 import BeautifulSoup as bs


class FirstSpiderSpider(scrapy.Spider):
    name = 'first_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://unsplash.com/s/photos/book']

    def parse(self, response):
        soup = bs(response.text, 'lxml')
        item = {
            'image_urls': []
        }
        for image in soup.find_all("img"):
            try:
                item['image_urls'].append(image['src'])
            except Exception:
                pass
        return item
