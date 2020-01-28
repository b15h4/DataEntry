import scrapy
from ..items import Century21Item
import xlsxwriter

class CenturySpider(scrapy.Spider):
    name = 'centuryspy'
    allowed_domains = ['century21.ca']
    pagenumber = 2
    start_urls = ['https://www.century21.ca/search/directory/Province-ON/page1']

    def parse(self,response):
        #Exctract
        Names = response.xpath("//li/a[@class='agent-name']/text()").extract()
        Phones = response.xpath("//li[@class='agent-phone-number']/text()").extract()
        Emails = response.xpath("//a[@class='agent-email']/@href").extract()
        Websites = response.xpath("//a[@class='agent-name']/@href").extract()        

        #Output
        for Name,Phone,Email,Website in zip(Names,Phones,Emails,Websites):
            item = Century21Item()
            item['Name'] = Name.strip()
            item['Phone'] = Phone[:14].strip()
            item['Email'] = Email.strip().replace('mailto:','')
            item['Website'] = response.urljoin(Website).strip()
            yield item

        #Next-Page
        next_page = f'https://www.century21.ca/search/directory/Province-ON/page{str(CenturySpider.pagenumber)}'       
        if CenturySpider.pagenumber <= 111:
            CenturySpider.pagenumber += 1          
            yield response.follow(url=next_page,callback=self.parse)