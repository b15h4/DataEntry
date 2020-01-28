from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://servicesenligne2.ville.montreal.qc.ca/sel/evalweb/index")

time.sleep(3)

driver.find_element_by_id("matricule").click()

time.sleep(5)

driver.close()