import scrapy 
from ..items import AirdrieItem
import csv
from scrapy.http import FormRequest

class AirDrieSpider(scrapy.Spider):
	name = 'airdriespy'

	def start_requests(self):
		NumbersLINC = []

		with open('numbers.csv', mode='r') as csv_file:
			csv_reader = csv.reader(csv_file)
			for row in csv_reader:
				NumbersLINC.append(row)

		for x in list(NumbersLINC):
			input1 = x[0]
			input2 = x[1]
			input3 = x[2]

			yield FormRequest('https://www.airdrie.ca/index.cfm?serviceid=284', formdata={'serviceid':'284','whichPlan': '{}'.format(input1), 'whichBlock':'{}'.format(input2), 'whichLot': '{}'.format(input3), 'legalSubmit': 'Search'}, callback=self.parse_items)

	def parse_items(self,response):

		item = AirdrieItem()
		Plan = response.xpath("//div[@class='datagrid']/table/tbody/tr[2]/td/text()[2]").extract_first()
		Block_Unit = response.xpath("//div[@class='datagrid']/table/tbody/tr[2]/td/text()[4]").extract_first()
		Lot = response.xpath("//div[@class='datagrid']/table/tbody/tr[2]/td/text()[6]").extract_first()

		Roll = response.xpath("//div[@class='datagrid']/table/tbody/tr[1]/td/text()").extract_first()
		Assessed_Value = response.xpath("//div[@class='datagrid']/table/tbody/tr[3]/td/text()").extract_first()
		Land_Use = response.xpath("//div[@class='datagrid']/table/tbody/tr[4]/td/text()").extract_first()
		Classifications = response.xpath("//div[@class='datagrid']/table/tbody/tr[5]/td/text()").extract_first()
		Parcel_Area = response.xpath("//div[@class='datagrid']/table/tbody/tr[6]/td/text()").extract_first()
		Year_Built = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[1]/td/text()").extract_first()
		
		Living_Area_above_Grade = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[2]/td/text()").extract_first()
		Building_Description = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[3]/td/text()").extract_first() # no strip
		Finished_Area_Below_Grade = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[4]/td/text()").extract_first() # strip
		Garage = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[5]/td/text()").extract_first()
		Deck_s = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[6]/td/text()").extract_first()
		Veranda_s = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[7]/td/text()").extract_first()
		Fireplace_s = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[8]/td/text()").extract_first() # strip
		Walkout_Basement = response.xpath("//table[@class='quickkey_tbl ']/tbody/tr[9]/td/text()").extract_first()

 

		try:
			if Plan == None:
				item['Plan'] = Plan
			else:
				item['Plan'] = Plan.strip()
			if Block_Unit == None:
				item['Block_Unit'] = Block_Unit
			else:
				item['Block_Unit'] = Block_Unit.strip()
			if  Lot == None:
				item['Lot'] = Lot
			else:
				item['Lot'] = Lot.strip()

			if Roll == None:
				item['Roll'] = Roll
			else:
				item['Roll'] = Roll.strip()
			if Assessed_Value == None:
				item['Assessed_Value'] = Assessed_Value
			else:
				item['Assessed_Value'] = Assessed_Value.strip()
			if Land_Use == None:
				item['Land_Use'] = Land_Use
			else:	
				item['Land_Use'] = Land_Use.strip()
			if Classifications == None:
				item['Classifications'] = Classifications
			else:
				item['Classifications'] = Classifications.strip()
			if Parcel_Area == None:
				item['Parcel_Area'] = Parcel_Area
			else:
				item['Parcel_Area'] = Parcel_Area.strip()
			if Year_Built == None:
				item['Year_Built'] = Year_Built
			else:
				item['Year_Built'] = Year_Built.strip()
			if Living_Area_above_Grade == None:
				item['Living_Area_above_Grade'] = Living_Area_above_Grade
			else:
				item['Living_Area_above_Grade'] = Living_Area_above_Grade.strip()
			if Building_Description == None:
				item['Building_Description'] = Building_Description
			else:
				item['Building_Description'] = Building_Description.strip()
			if Finished_Area_Below_Grade == None:
				item['Finished_Area_Below_Grade'] = Finished_Area_Below_Grade
			else:
				item['Finished_Area_Below_Grade'] = Finished_Area_Below_Grade.strip()
			if Garage == None:
				item['Garage'] = Garage
			else:
				item['Garage'] = Garage.strip()
			if Deck_s == None:
				item['Deck_s'] = Deck_s
			else:
				item['Deck_s'] = Deck_s.strip()
			if Veranda_s == None:	
				item['Veranda_s'] = Veranda_s
			else:
				item['Veranda_s'] = Veranda_s.strip()
			if Fireplace_s == None:
				item['Fireplace_s'] = Fireplace_s
			else:
				item['Fireplace_s'] = Fireplace_s.strip()
			if Walkout_Basement == None:
				item['Walkout_Basement'] = Walkout_Basement
			else:
				item['Walkout_Basement'] = Walkout_Basement.strip()

			if Plan != None:
				yield item
		except:
			pass