import scrapy
from ..items import TargetspiderItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TargetSpider(scrapy.Spider):
	name = 'targetspy'
	pagenumber = 0
	start_urls = ['https://www.target.com/c/beauty-gift-ideas/-/N-54x8k?lnk=MothersDayBeaut&Nao=0']

	
	def __init__(self):
		self.driver = webdriver.Firefox()

	def parse(self,response):
		while self.pagenumber <= 768:
			url = 'https://www.target.com/c/beauty-gift-ideas/-/N-54x8k?lnk=MothersDayBeaut&Nao={}'.format(self.pagenumber)
			self.driver.get(url)
			time.sleep(10)
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(1)
			Links = []
			Link = self.driver.find_elements_by_xpath("//a[@data-test='product-title']")

			for x in Link:
				Links.append(x.get_attribute('href'))

			for url in Links:
				try:
					self.driver.get(url)
					time.sleep(1)
					self.driver.find_element_by_xpath("//button[@data-test='toggleContentButton']").click()
					time.sleep(1)
					Highlights = self.driver.find_elements_by_xpath("//div[@data-test='detailsTab']")

					item = TargetspiderItem()



					for high in Highlights:
						item['Details'] = high.text

					try:
						self.driver.find_element_by_id('tab-Drugfacts').click()

						DrugFacts = self.driver.find_elements_by_xpath("//div[@class='h-margin-t-default h-padding-h-default']")

						for drug in DrugFacts:
							item['DrugFacts'] = drug.text
					except:
						pass

					Brand = self.driver.find_element_by_xpath('//div[@class="styles__ProductDetailsTitleRelatedLinks-sc-12eg98-0 eVTLYK"]/a[@class="Link-sc-1khjl8b-0 ftgTJf"]/span').text
					Price = self.driver.find_element_by_xpath("//div[@class='h-padding-h-default h-padding-t-tight']/div/span[@data-test='product-price']").text
					ProductName = self.driver.find_element_by_xpath("//h1[@class='h-margin-b-none h-margin-b-tiny h-text-normal h-margin-t-tiny Heading__StyledHeading-sc-6yiixr-0 fvUlBv']/span").text
					StarRating = self.driver.find_element_by_xpath("//div[@class='h-text-bold RatingSummary__StyledRating-bxhycp-0 KugPU']").text
					Category = self.driver.find_elements_by_xpath("//a[@class='Link-sc-1khjl8b-0 iSPUUR']/span")
					NumberofReviews = self.driver.find_element_by_xpath("//span[@class='h-text-sm h-margin-l-tiny Count__FeedbackCount-g0guvt-0 fNvZwe']/span").text

					item['Brand'] = Brand.replace("Shop all" , "").strip()
					item['Price'] = Price
					item['ProductName'] = ProductName
					item['ProductLink'] = url
					item['Category'] = Category[1].text
					item['SubCategory'] = Category[2].text
					item['StarRating'] = StarRating
					item['NumberofReviews'] = NumberofReviews
					try:
						item['Path'] = Category[0].text + '/' + Category[1].text + '/' + Category[2].text  + '/' + Category[3].text
					except:
						item['Path'] = Category[0].text + '/' + Category[1].text + '/' + Category[2].text

					yield item
				except:
					pass
			self.pagenumber+=24
			Links.clear()

		self.driver.close()

