import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from urllib.request import urlopen
from bs4 import BeautifulSoup

webpage = r"http://www.nitt.edu/prm/nitreg/ShowRes.aspx"

a = sys.argv[1]
b = sys.argv[2]
for roll in range(int(a), int(b)):
	searchterm = str(roll)
	driver = webdriver.Chrome("/path/to/chromedriver")
	driver.get(webpage)
	sbox = driver.find_element_by_id("TextBox1")
	sbox.send_keys(searchterm)
	sbox.send_keys(Keys.ENTER)
	try:
		select = Select(driver.find_element_by_id("Dt1"))
		select.select_by_value("137")
		html = driver.page_source
		driver.quit()
		soup = BeautifulSoup(html, 'html.parser')
		try:
			print(soup.find_all('span')[1].b.string, ',', soup.find_all('span')[2].b.string, ',', soup.find_all('span')[5].b.string)
		except:
			driver.quit()
			continue
	except:
		driver.quit()
		continue
