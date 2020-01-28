import scrapy


class AirGunSpider(scrapy.Spider):
	name = 'airgunspy'

	start_urls = ['https://www.airgundepot.com/airgunpellets.html']

	def parse(self,response):

		Links = response.xpath("//div[@class='item-box']/a/@href").extract()

		yield {'Links' : response.body}