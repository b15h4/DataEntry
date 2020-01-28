import scrapy
import csv
from ..items import MontrealItem
from scrapy.http import FormRequest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class MontReal(scrapy.Spider):
	name = 'montspy'

	# start_urls = ['https://servicesenligne2.ville.montreal.qc.ca/sel/evalweb/obtenirMatriculesPourNumero']

	# def parse(self,response):
	# 	yield scrapy.FormRequest.from_response(response, meta={'solve_captcha': True},formdata={'searchType': 'searchByMatricule','HTML_FORM_FIELD':'CZ5bbg'},callback=self.parse_items)

	# def parse_items(self,response):
		
	# 	yield {'response' : response.body}
	def parse(self, response):
		url = 'https://servicesenligne2.ville.montreal.qc.ca/sel/evalweb/index'
		yield scrapy.Request(url, callback=self.parse_captchad, meta={'solve_captcha':True})

	def parse_captchad(self,response):
		solved = response['solved']
		yield {'response': solved}