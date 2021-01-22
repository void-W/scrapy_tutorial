import scrapy
from bs4 import BeautifulSoup as bs


class FirstSpiderSpider(scrapy.Spider):
    name = 'first_spider'
    allowed_domains = ['baidu.com']

    def start_requests(self):
        yield scrapy.Request("https://unsplash.com/s/photos/book", headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'})

    def parse(self, response):
        soup = bs(response.text, 'lxml')
        item = {
            'image_urls': []
        }
        for image in soup.find_all("img"):
            try:
                url = image['src']
                if "http" in url:
                    item['image_urls'].append(url)
            except Exception:
                pass
        return item
