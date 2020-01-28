import scrapy
from ..items import TransfermarketItem
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options
import csv

class TransferMarketSpider(scrapy.Spider):
	name = 'transferspy'

	start_urls = ['https://www.google.com']

	def parse(self,response):
		chrome_options = Options()  
		chrome_options.add_argument("--headless")

		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		url = []
		with open('links.txt', mode='r') as txt_file:
			reader = csv.reader(txt_file)
			for row in reader:
				if not row:
					pass
				else:
					url.append(','.join(row))

		for numerolinko in url:
			self.driver.get(numerolinko)
			time.sleep(1)
			club_name = self.driver.find_elements_by_xpath("//td[@class='hauptlink no-border-links']/a")
			loan_players = self.driver.find_elements_by_xpath("//td[@class='zentriert hauptlink']/a")
			average_loan_period_in_years = self.driver.find_elements_by_xpath("//tbody/tr/td[4]")
			appearances = self.driver.find_elements_by_xpath("//tbody/tr/td[5]")
			starting_formation = self.driver.find_elements_by_xpath("//tbody/tr/td[6]")
			goals = self.driver.find_elements_by_xpath("//tbody/tr/td[7]")
			average_minutes_played = self.driver.find_elements_by_xpath("//tbody/tr/td[8]")
			loan_fee = self.driver.find_elements_by_xpath("//tbody/tr/td[9]")
			market_value_at_start_of_loan = self.driver.find_elements_by_xpath("//tbody/tr/td[10]")

			item = TransfermarketItem()
			
			for x,y,z,zh,n,m,r,q,s in zip(club_name, loan_players, average_loan_period_in_years, appearances, starting_formation, goals, average_minutes_played, loan_fee, market_value_at_start_of_loan):
				item['club_name'] = x.get_attribute('title')
				item['loan_players'] = y.text
				item['average_loan_period_in_years'] = z.text
				item['club_link_TFM'] = x.get_attribute('href')
				item['loan_players_link'] = y.get_attribute('href')
				item['appearances'] = zh.text
				item['starting_formation'] = n.text
				item['goals'] = m.text
				item['average_minutes_played'] = r.text
				item['loan_fee'] = q.text
				item['market_value_at_start_of_loan'] = s.text



				filter_loan_type_TFM = re.findall('war', str(numerolinko))
				filter_season_id_TFM = re.findall('[0-9][0-9][0-9][0-9]', str(numerolinko))

				if 'war' in filter_loan_type_TFM:
					item['filter_loan_type_TFM'] = 'in on loan'
				else:
					item['filter_loan_type_TFM'] = 'out on loan'

				for fil in filter_season_id_TFM:
					item['filter_season_id_TFM'] = int(fil)+1

				yield item