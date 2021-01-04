from selenium import webdriver
import time
import yaml

def explore_list(sessionId, steamLoginSecure, options, first, second) -> bool:

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
		try:
			browser.find_element_by_class_name('discover_queue_empty_refresh_btn').click()
		except:
			browser.close()
			print("Invalid Cookie or some network error! (Cookie could be invalid => need to replace with new one)")
			return False

	i = 0
	j = 0
	
	while i < first:
		retries = 0
		while j <= second:
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
						retries += 1
						if retries > 3:
							print("Too many errors when clicking through list!")
							browser.close()
							return False
						print("Some error happened. Retrying after 5 sec.")
						time.sleep(1)

		i += 1

	browser.close()
	return True

def main():

	with open("config.yml", "r") as ymlfile:
		cfg = yaml.safe_load(ymlfile)

	options = webdriver.FirefoxOptions()
	options.add_argument('--headless')

	first = cfg['loops']['first']
	second = cfg['loops']['second']

	for num,account in enumerate(cfg['steam']):

		res = explore_list(account['sessionId'], account['steamLoginSecure'], options, first, second)

		if res:
			print(f'Finished account {num}!')

if __name__ == "__main__":
    main()