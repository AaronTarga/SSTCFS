from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(executable_path='chromedriver.exe' , chrome_options=options)
cookie = {'name' : 'sessionId' , 'value' : '...'}
cookie2 = {'name' : 'steamLoginSecure', 'value' : '...'}
cookie3 = {'name': 'webTradeEligibility','value': '...'}
browser.get('link to your inventory')
browser.add_cookie(cookie)
browser.add_cookie(cookie2)
browser.add_cookie(cookie3)
browser.get('link to your inventory')
browser.find_element_by_class_name('global_action_link').click()
time.sleep(1)
browser.save_screenshot("screenshot.png")
try:
	i = 0
	while i < int(browser.find_element_by_id('pagecontrol_max').text):
		for item in browser.find_elements_by_class_name('itemHolder'):
			if item.is_displayed():
				time.sleep(0.1)
				if browser.find_element_by_id('iteminfo1_item_type').text == 'item name you want to sell':
					time.sleep(1)
					print(browser.find_element_by_id('iteminfo1_item_type').text)
					time.sleep(1)
					browser.find_element_by_class_name('item_market_action_button').click()
					time.sleep(1)
					browser.find_element_by_id("market_sell_buyercurrency_input").clear()
					browser.find_element_by_id("market_sell_buyercurrency_input").send_keys('for how much you wanna sell it (0,05$ for example)')
					if browser.find_element_by_id("market_sell_dialog_accept_ssa").is_selected() is not True:
						browser.find_element_by_id('market_sell_dialog_accept_ssa').click()
					try:
						browser.find_element_by_id('market_sell_dialog_accept').click()
					except:
						a = 0
				try:
					item.click()
				except Exception as e:
					a = 1
		browser.find_element_by_id("pagebtn_next").click()
		i += 1
		print(i)
except Exception as e:
	print(e)
time.sleep(5)
browser.close()
