from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.transfermarkt.com/league-of-ireland/leihspieler/wettbewerb/IR1/plus/1?saison_id=2018&leihe=war")

Name = driver.find_elements_by_xpath("//td[@class='hauptlink no-border-links']/a")

for x in Name:
	print(x.get_attribute('title'))

time.sleep(2)
driver.close()