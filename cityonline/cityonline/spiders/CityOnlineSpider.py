import scrapy
from ..items import CityonlineItem
import csv
import json
import re

class CityOnlineSpider(scrapy.Spider):
	name = 'onlinespy'

	start_urls = []
	
	NumbersLINC = []
	with open('numbers.csv', mode='r') as csv_file:
				csv_reader = csv.reader(csv_file)
				for row in csv_reader:
					if not row:
						pass
					else:
						NumbersLINC.append(','.join(row))

	for linc in NumbersLINC:
		start_urls.append('https://cityonline.calgary.ca/GISMap/proxy/CacheService.ashx?ptype=searchbylinc&linc={}&f=json'.format(linc))
	

	def parse(self,response):

		jsonresponse = json.loads(response.body_as_unicode())

		stringlist = jsonresponse['stringlist']
		LINC = re.findall('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', str(response))
		Output = stringlist[0]

		item = CityonlineItem()

		item['LINC'] = LINC[0]
		item['Address'] = Output.replace(':',' ').strip()
		yield item
