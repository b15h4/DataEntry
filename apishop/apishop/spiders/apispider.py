import scrapy
from ..items import ApishopItem
import csv
import time
import json

class ApishopSpider(scrapy.Spider):
	name = 'apispy'
	start_urls = []

	with open('list1.csv', mode='r') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			if not row:
				pass
			else:
				start_urls.append(','.join(row))

	def parse(self,response):
		try:
			jsonresponse = json.loads(response.body_as_unicode())
			data = jsonresponse['data']
			datainside = data['items']

			datalist = datainside[0]
			salesprices = datalist['salesPrices']
			prices = salesprices[0]
			customFields = datalist['customFields']
			
			

			item = ApishopItem()

			item['ArticleNumber'] = datalist['id']
			item['expectedDeliveryDateFormatted'] = datalist['expectedDeliveryDateFormatted']
			item['AvailableQty'] = customFields['Available Qty. 3']
			item['quantityFormatted'] = prices['quantityFormatted']
			item['inventoryCount'] = datalist['inventoryCount']
			item['inventoryCountFormatted'] = datalist['inventoryCountFormatted']
			
			
			yield item
		except:
			pass