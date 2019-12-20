from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1920x1080')
browser = webdriver.Chrome(executable_path='chromedriver' , chrome_options=options)
browser.get('https://store.steampowered.com/')
cookie = {'name' : 'sessionId' , 'value' : '...'}
cookie2 = {'name' : 'steamLoginSecure', 'value' : '...'}
browser.add_cookie(cookie)
browser.add_cookie(cookie2)
browser.get('https://store.steampowered.com/')
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
try:
	browser.find_element_by_id("discovery_queue_start_link").click()
except:
	browser.find_element_by_class_name('discover_queue_empty_refresh_btn').click()
i = 0
while i < 3:
	j = 0
	while j < 12:
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
					print('hehe')
	i += 1
	print(i)
browser.close()