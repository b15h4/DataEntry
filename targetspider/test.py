from selenium import webdriver
import time 

driver = webdriver.Chrome()

driver.get('https://www.target.com/c/beauty-gift-ideas/-/N-54x8k?lnk=MothersDayBeaut')
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

Links = []

Link = driver.find_elements_by_xpath("//a[@data-test='product-title']")

Brand = driver.find_element_by_xpath('//div[@class="styles__ProductDetailsTitleRelatedLinks-sc-12eg98-0 eVTLYK"]/a[@class="Link-sc-1khjl8b-0 ftgTJf"]/span').text

Price = driver.find_element_by_xpath("//div[@class='h-padding-h-default h-padding-t-tight']/div/span[@data-test='product-price']").text

ProductNames = driver.find_element_by_xpath("//h1[@class='h-margin-b-none h-margin-b-tiny h-text-normal h-margin-t-tiny Heading__StyledHeading-sc-6yiixr-0 fvUlBv']/span").text

StarRatings = driver.find_element_by_xpath("//div[@class='h-text-bold RatingSummary__StyledRating-bxhycp-0 KugPU']").text

Category = driver.find_elements_by_xpath("//a[@class='Link-sc-1khjl8b-0 iSPUUR']/span")

NumberofReviews = driver.find_element_by_xpath("//span[@class='h-text-sm h-margin-l-tiny Count__FeedbackCount-g0guvt-0 fNvZwe']/span").text

for x in Link:
	Links.append(x.get_attribute('href'))


for x in Links:
	driver.get(x)
	time.sleep(3)
	driver.find_element_by_xpath("//button[@data-test='toggleContentButton']").click()
	time.sleep(3)
	Highlights = driver.find_elements_by_xpath("//div[@data-test='detailsTab']")
	for x in Highlights:
		itemhigh = x.text
	try:
		driver.find_element_by_id('tab-Drugfacts').click()

		DrugFact = driver.find_elements_by_xpath("//div[@class='h-margin-t-default h-padding-h-default']")

		for x in DrugFact:
			print(x.text)
	except:
		pass


driver.close()