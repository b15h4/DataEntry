import scrapy
from ..items import CapterraItem

class CapterraSpider(scrapy.Spider):
    name = 'capterra'

    start_urls = ['https://www.capterra.com/applicant-tracking-software/']

    def parse(self,response):

        names = response.xpath("//h2[@class='listing-name']/a/text()").extract()
        authors = response.xpath("//h3[@class='epsilon  listing-vendor']/text()").extract()
        #descriptions = response.xpath("//p[@class='listing-description  milli hide-palm']/text()").extract()
        
        items = []
        for name, author in zip(names,authors):
            item = CapterraItem()
            item['author'] = author.strip()
            item['name'] = name.strip()
            items.append(item)
        return items