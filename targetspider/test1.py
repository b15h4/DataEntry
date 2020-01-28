from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get('https://www.target.com/p/love-beauty-planet-murumuru-butter-and-rose-oil-hand-and-body-lotion-13-5oz/-/A-75558431')

ProductNames = driver.find_element_by_xpath("//h1[@class='h-margin-b-none h-margin-b-tiny h-text-normal h-margin-t-tiny Heading__StyledHeading-sc-6yiixr-0 fvUlBv']/span").text

StarRatings = driver.find_element_by_xpath("//div[@class='h-text-bold RatingSummary__StyledRating-bxhycp-0 KugPU']").text

Category = driver.find_elements_by_xpath("//a[@class='Link-sc-1khjl8b-0 iSPUUR']/span")

NumberofReviews = driver.find_element_by_xpath("//span[@class='h-text-sm h-margin-l-tiny Count__FeedbackCount-g0guvt-0 fNvZwe']/span").text

print(Category[0].text)

driver.close()