import scrapy
from scrapy_splash import SplashRequest

class CanadaSpider(scrapy.Spider):
    name = 'canadashit'

    def parse_requests(self):
        url = 'https://www.century21.ca/search/directory/Province-ON'
        yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={'wait':0.5})
    
    def parse(self,response):
        for li in response.xpath("//div/div/div/ul/li"):
            yield {
                'name' : li.xpath("/a[@class='agent-name']/text()").extract_first()
            }