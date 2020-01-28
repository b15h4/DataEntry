import scrapy
from ..items import CbcworldItem

class CbcSpider(scrapy.Spider):
	name = 'cbcspy'
	page = 2
	start_urls = ['https://www.cbcworldwide.com/professionals/find']

	def parse(self,response):
		for url in response.xpath("//div[@class='card-row']/a/@href").extract():
			yield response.follow(url,callback=self.parse_items)
	
	def parse_items(self,response):

		Names = response.xpath("//div[@class='primary-contact person']/h3/a/text()").extract()
		Offices = response.xpath("//div[@class='office-name']/h5/a/text()[1]").extract()
		Addresses = response.xpath("//div[@class='office-address']/a/div/text()").extract()
		Emails = response.xpath("//div[@class='contact-info']/a[@data-ga-click-action='view-professional-email']/text()").extract()

		for Name,Office,Address,Email in zip(Names,Offices,Addresses,Emails):
			item = CbcworldItem()

			item['Name'] = Name.strip()
			item['Office'] = Office.strip()
			item['Address'] = Address.strip()
			item['Email'] = Email.strip().lower()
			yield item

		next_pagge = f'https://www.cbcworldwide.com/professionals/find?page={str(CbcSpider.page)}'

		if CbcSpider.page <= 100:
			CbcSpider.page +=1

			yield response.follow(url=next_pagge,callback=self.parse)