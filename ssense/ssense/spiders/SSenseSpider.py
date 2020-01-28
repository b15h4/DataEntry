import scrapy
from ..items import SsenseItem

class SSenseSpider(scrapy.Spider):
    name = 'ssensespy'
    pagenumber = 2
    start_urls = ['https://www.ssense.com/en-ch/women?gclid=EAIaIQobChMI4qqW59O24QIViqoYCh3k_ghnEAAYASAAEgJ9GvD_BwE&page=1']

    def parse(self,response):
        Titles = response.xpath("//figcaption/p[@itemprop='brand']/text()").extract()
        Prices = response.xpath("//div/p/span/text()").extract()
        Descriptions = response.xpath("//figcaption/p[@itemprop='name']/text()").extract()
        Urls = response.xpath("//figure/a/@href").extract()
        Images = response.xpath("//img/@src").extract()

        for Title,Price,Description,Url,Image in zip(Titles,Prices,Descriptions,Urls,Images):
            item = SsenseItem()
            item['Title'] = Title.strip()
            item['Price'] = Price.strip().replace('€','$')
            item['Description'] = Description.strip()
            item['Url'] = response.urljoin(Url).strip()
            item['Image'] = Image.strip()
            yield item
    
        next_page = f'https://www.ssense.com/en-ch/women?gclid=EAIaIQobChMI4qqW59O24QIViqoYCh3k_ghnEAAYASAAEgJ9GvD_BwE&page={str(SSenseSpider.pagenumber)}'
        if SSenseSpider.pagenumber <= 234:
            SSenseSpider.pagenumber += 1
            yield response.follow(url=next_page,callback=self.parse)
