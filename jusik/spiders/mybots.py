import scrapy
from jusik.items import JusikItem


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/main.nhn?code=005930']
    start_urls = ['http://finance.naver.com/item/main.nhn?code=005930']

    def parse(self, response):
        codes =  response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        blinds = response.css('.blind::text').extract()

        items = []
        item = JusikItem()
        item['code']=codes[0]      
        item['price'] = blinds[36]
        item['total']= blinds[42]
        item['high'] = blinds[40]
        item['low'] = blinds[44]
        items.append(item)
        
        return items
