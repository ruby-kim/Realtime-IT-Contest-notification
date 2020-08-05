from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

sitepath = "https://thinkcontest.com"
chromepath = "./.lib/chromedriver.exe"
contestTitles = []
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(chromepath, options=options)
driver.implicitly_wait(3)

driver.get(sitepath)

# for i in range(1, 10):
tb = driver.find_element_by_class_name("type-2.mg-t-5.contest-table")

for tr in tb.find_element_by_tag_name("tr"):
	title = tr.find_element_by_tag_name('a')
	print(title.text)
driver.quit()
