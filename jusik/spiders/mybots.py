import scrapy
from jusik.items import JusikItem


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/main.nhn?code=005930']
    start_urls = ['http://finance.naver.com/item/main.nhn?code=005930']

    def parse(self, response):
        codes =  response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        prices = response.xpath('//*[@id="chart_area"]/div[1]/div/p[1]/em/span[1]/text()').extract()
        totals = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/em/text()').extract()
        blinds = response.css('.blind::text').extract()

        items = []
        for idx in range(len(codes)):
            item = JusikItem()
            item['code']=codes[idx]
            item['price'] = prices[idx]
            item['total']= totals[idx]
            item['high'] = blinds[idx * 40 +40]
            item['low'] = blinds[idx * 40 +44]
            items.append(item)
        return items
