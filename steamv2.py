from selenium import webdriver
import time
import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')

browser = webdriver.Firefox(options=options)
browser.get('https://store.steampowered.com/')

cookie = {'name' : 'sessionId' , 'value' : cfg['steam']['sessionId']}
cookie2 = {'name' : 'steamLoginSecure', 'value' : cfg['steam']['steamLoginSecure']}

browser.add_cookie(cookie)
browser.add_cookie(cookie2)
browser.get('https://store.steampowered.com/')
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

try:
	browser.find_element_by_id("discovery_queue_start_link").click()
except:
	browser.find_element_by_class_name('discover_queue_empty_refresh_btn').click()

i = 0
j = 0

while i < cfg['loops']['first']:
	while j < cfg['loops']['second']:
		try:
			browser.find_element_by_class_name('btn_next_in_queue').click()
			j += 1
		except:
			try:
				browser.find_element_by_class_name('discover_queue_empty_refresh_btn').click()
			except:
				try:
					browser.find_element_by_class_name('refresh_queue_btn').click()
				except:
					print('error')
	i += 1

browser.close()