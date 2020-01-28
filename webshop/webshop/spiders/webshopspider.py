import scrapy
from ..items import WebshopItem
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

class WebShopSpider(scrapy.Spider):
	name = 'webspy'
	pagenumber = 1
	start_urls = ['https://webshopb2b.bloomingville.com/customers/customer_login.aspx']

	def __init__(self):
		

		self.driver = webdriver.Chrome()

	def parse(self, response):
		self.driver.get(response.url)
		username = self.driver.find_element_by_id("ctl00_plhContent_ctl01_ctl00_txtUsername")
		username.clear()
		username.send_keys("4902100")

		password = self.driver.find_element_by_id("ctl00_plhContent_ctl01_ctl00_txtPassword")
		password.clear()
		password.send_keys("67jXFqVVyScUQ9q")

		self.driver.find_element_by_name("ctl00$plhContent$ctl01$ctl00$btnLogin").click()

		try:
			while self.pagenumber <= 6:
				url = "https://webshopb2b.bloomingville.com/pl/Essentials_161978.aspx?page={}".format(self.pagenumber)
				self.driver.get(url)
				elems = self.driver.find_elements_by_xpath("//div[@class='product-list-container active']/ul/li/div/div[@class='productName']/a[@href]")
				product_links = []
			
				for x in elems:
					product_links.append(x.get_attribute('href'))

				for y in product_links:
					self.driver.get(y)
					opendesc = self.driver.find_element_by_xpath("//ul[@class='accordion']/li/a[@href]").click()
					time.sleep(2)

					item = WebshopItem()

					Description = self.driver.find_element_by_class_name("accordion")
					divs = Description.find_elements_by_xpath("//div[@id='panel3a']")

					ImageLink = self.driver.find_elements_by_xpath("//ul[@class='product-image-thumbnails']/li/img[@src]")
					try:
						num_page_items = len(divs)
						for i in range(num_page_items):					
							item['Description'] = divs[i].text
					
						ImageSave = []
						for x in ImageLink:
							ImageSave.append(x.get_attribute('src'))
							item['Images'] = ImageSave

						Title = self.driver.find_element_by_xpath("//h1[@itemprop='name']").text
						ArticleNumber = self.driver.find_element_by_xpath("//div[@class='ext-itemnr']").text.replace("Artikelnummer:","").strip()
						Price = self.driver.find_element_by_xpath("//span[@class='tag-price-normal']").text
						SpecialPrice = self.driver.find_element_by_xpath("//div[@class='ProductListPriceValue']").text.replace("UVP:","").strip()
						MinimumQuantity = self.driver.find_element_by_xpath("//div[@class='colli-qty']").text.replace("Anzahl per Kolli:","").strip()

						item['Title'] = Title
						item['ArticleNumber'] = ArticleNumber
						item['Price'] = Price
						item['SpecialPrice'] = SpecialPrice
						item['MinimumQuantity'] = MinimumQuantity

						yield item
					except:
						pass
		
			self.driver.get(url)

			nextpage = self.driver.find_element_by_xpath("//div[@class='list-pager']/div/span/a[@class='nextPageLnk']")
			if nextpage:
				nextpage.click()
				time.sleep(1)
				self.pagenumber += 1
				product_links.clear()

		except:
			pass		

		self.driver.close()