from selenium import webdriver
import time
import yaml

def explore_list(sessionId, steamLoginSecure, options, first, second):

	cookie = {'name' : 'sessionId' , 'value' : sessionId }
	cookie2 = {'name' : 'steamLoginSecure', 'value' : steamLoginSecure }

	browser = webdriver.Firefox(options=options)

	browser.get('https://store.steampowered.com/explore/')
	browser.add_cookie(cookie)
	browser.add_cookie(cookie2)
	browser.get('https://store.steampowered.com/explore/')

	try:
		browser.find_element_by_id("discovery_queue_start_link").click()
	except:
		browser.find_element_by_class_name('discover_queue_empty_refresh_btn').click()

	i = 0
	j = 0

	while i < first:
		while j < second:
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
						print("Some error happened. Retrying after 1 sec.")
						sleep(1)
						
		i += 1

	browser.close()

def main():

	with open("config.yml", "r") as ymlfile:
		cfg = yaml.safe_load(ymlfile)

	options = webdriver.FirefoxOptions()
	options.add_argument('--headless')
	options.add_argument('window-size=1920x1080')

	first = cfg['loops']['first']
	second = cfg['loops']['second']

	for num,account in enumerate(cfg['steam']):
		explore_list(account['sessionId'], account['steamLoginSecure'], options, first, second)
		print(f'finished account {num}')

if __name__ == "__main__":
    main()