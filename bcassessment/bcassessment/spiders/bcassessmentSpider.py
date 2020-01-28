import scrapy
import csv
from ..items import BcassessmentItem
import json
import time

class newBcassesmentSpider(scrapy.Spider):
	name = 'basespy'

	def start_requests(self):
		PID = []

		with open('Kelowna-for-B-links.csv', mode='r') as csv_file:
			csv_reader = csv.reader(csv_file)
			for row in csv_reader:
				if not row:
					pass
				else:
					PID.append(','.join(row))
		
		for iii in PID:
			yield scrapy.Request('https://www.bcassessment.ca//Property/Info/{}'.format(iii), callback=self.parse_items)

	def parse_items(self,response):
		try:
			item = BcassessmentItem()
			PID = response.xpath("//div[@id='lblLegalDescription']/p[2]/text()").extract_first().replace("PID:","").strip()
			Address = response.xpath("//h1[@id='mainaddresstitle']/text()").extract_first()			
			Area_Jurisdiction_Roll = response.xpath("//span[@id='areajursrolltitlebox']/text()").extract_first().replace("Area-Jurisdiction-Roll:","")
			Total_Value = response.xpath("//span[@id='lblTotalAssessedValue']/text()").extract_first()
			Land = response.xpath("//p[@id='lblTotalAssessedLand']/text()").extract_first()
			Buildings = response.xpath("//p[@id='lblTotalAssessedBuilding']/text()").extract_first()
			Previous_Year_Value = response.xpath("//p[@id='lblPreviousAssessedValue']/text()").extract_first()
			Previous_Land = response.xpath("//p[@id='lblPreviousAssessedLand']/text()").extract_first()
			Previous_Buildings = response.xpath("//p[@id='lblPreviousAssessedBuilding']/text()").extract_first()
			Year_Built = response.xpath("//td[@id='lblYearBuilt']/text()").extract_first()			
			Description = response.xpath("//td[@id='lblDescription']/text()").extract_first()
			Bedrooms = response.xpath("//td[@id='lblBedrooms']/text()").extract_first()
			Bathrooms = response.xpath("//td[@id='lblBathRooms']/text()").extract_first()
			Carports = response.xpath("//td[@id='lblCarPorts']/text()").extract_first()
			Garages = response.xpath("//td[@id='lblGarages']/text()").extract_first()
			Land_Size = response.xpath("//td[@id='lblLandSize']/text()").extract_first()
			First_Flor_Area = response.xpath("//td[@id='lblFirstFloorArea']/text()").extract_first()
			Second_Flor_Area = response.xpath("//td[@id='lblSecondFloorArea']/text()").extract_first()
			Basement_Finish_Area = response.xpath("//td[@id='lblBasementFinishArea']/text()").extract_first()
			Strata_Area = response.xpath("//td[@id='lblStrataTotalArea']/text()").extract_first()
			Building_Storeys = response.xpath("//td[@id='lblStoriesBuilding']/text()").extract_first()
			Gross_Leasable_Area = response.xpath("//td[@id='lblGrossLeasableArea']/text()").extract_first()
			Net_Leasable_Area = response.xpath("//td[@id='lblNetLeasableArea']/text()").extract_first()
			No_Of_Apartament_Units = response.xpath("//td[@id='lblNumberUnitApartment']/text()").extract_first()
			Legal_Description_and_Parcel_ID = response.xpath("//div[@id='lblLegalDescription']/p[1]/text()").extract_first()
			Sold_Date = response.xpath("//tr[@class='salesrow']/td[1]/text()").extract_first()
			Sold_Price = response.xpath("//tr[@class='salesrow']/td[2]/text()").extract_first()

			if PID:
				item['PID'] = PID.strip()
			else:
				item['PID'] = PID
			if Address:
				item['Address'] = Address.strip()
			else:
				item['Address'] = Address
			if Description:
				item['Description'] = Description.strip()
			else:
				item['Description'] = Description
			if Bedrooms:
				item['Bedrooms'] = Bedrooms.strip()
			else:
				item['Bedrooms'] = Bedrooms
			if Bathrooms:
				item['Bathrooms'] = Bathrooms.strip()
			else:
				item['Bathrooms'] = Bathrooms
			if Carports:
				item['Carports'] = Carports.strip()
			else:
				item['Carports'] = Carports
			if Garages:	
				item['Garages'] = Garages.strip()
			else:
				item['Garages'] = Garages
			if Land_Size:
				item['Land_Size'] = Land_Size.strip()
			else:
				item['Land_Size'] = Land_Size
			if First_Flor_Area:
				item['First_Flor_Area'] = First_Flor_Area.strip()
			else:
				item['First_Flor_Area'] = First_Flor_Area
			if Second_Flor_Area:
				item['Second_Flor_Area'] = Second_Flor_Area.strip()
			else:
				item['Second_Flor_Area'] = Second_Flor_Area
			if Basement_Finish_Area:
				item['Basement_Finish_Area'] = Basement_Finish_Area.strip()
			else:
				item['Basement_Finish_Area'] = Basement_Finish_Area
			if Strata_Area:
				item['Strata_Area'] = Strata_Area.strip()
			else:
				item['Strata_Area'] = Strata_Area
			if Building_Storeys:
				item['Building_Storeys'] = Building_Storeys.strip()
			else:
				item['Building_Storeys'] = Building_Storeys
			if Gross_Leasable_Area:	
				item['Gross_Leasable_Area'] = Gross_Leasable_Area.strip()
			else:
				item['Gross_Leasable_Area'] = Gross_Leasable_Area
			if Net_Leasable_Area:
				item['Net_Leasable_Area'] = Net_Leasable_Area.strip()
			else:
				item['Net_Leasable_Area'] = Net_Leasable_Area
			if No_Of_Apartament_Units:
				item['No_Of_Apartament_Units'] = No_Of_Apartament_Units.strip()
			else:
				item['No_Of_Apartament_Units'] = No_Of_Apartament_Units
			if Sold_Date:
				item['Sold_Date'] = Sold_Date.strip()
			else:
				item['Sold_Date'] = Sold_Date
			if Sold_Price:
				item['Sold_Price'] = Sold_Price.strip()
			else:
				item['Sold_Price'] = Sold_Price

			if Total_Value:
				item['Total_Value'] = Total_Value.strip()
			else:
				item['Total_Value'] = Total_Value
			if Land:
				item['Land'] = Land.strip()
			else:
				item['Land'] = Land
			if Buildings:
				item['Buildings'] = Buildings.strip()
			else:
				item['Buildings'] = Buildings
			if Previous_Year_Value:
				item['Previous_Year_Value'] = Previous_Year_Value.strip()
			else:
				item['Previous_Year_Value'] = Previous_Year_Value
			if Previous_Land:
				item['Previous_Land'] = Previous_Land.strip()
			else:
				item['Previous_Land'] = Previous_Land
			if Previous_Buildings:
				item['Previous_Buildings'] = Previous_Buildings.strip()
			else:
				item['Previous_Buildings'] = Previous_Buildings
			if Year_Built:
				item['Year_Built'] = Year_Built.strip()
			else:
				item['Year_Built'] = Year_Built
			if Legal_Description_and_Parcel_ID:
				item['Legal_Description_and_Parcel_ID'] = Legal_Description_and_Parcel_ID.strip()
			else:
				item['Legal_Description_and_Parcel_ID'] = Legal_Description_and_Parcel_ID

			if Area_Jurisdiction_Roll:
				item['Area_Jurisdiction_Roll'] = Area_Jurisdiction_Roll.strip()
			else:
				item['Area_Jurisdiction_Roll'] = Area_Jurisdiction_Roll
			yield item
		except:
			pass