from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Add user and password login
login_email = '<<add login email>>'
login_password = '<<add password>>'

# open chromedriver from main folder
driver = webdriver.Chrome('C:/GitHub/ExperianCoffee/chromedriver')
time.sleep(2)

# navigate to login page
driver.get('https://database.coffeeinstitute.org/login')
time.sleep(2)

# submit login credentials 
form = driver.find_element_by_xpath('//html/body/content[@class="scrollable"]/div[@class="container page"]/div[@class="form short"]/div[@class="login panel"]/form')
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
time.sleep(2)

username.send_keys(login_email)
password.send_keys(login_password)
driver.find_element_by_class_name("submit").click()
time.sleep(2)


# navigate to coffees page, then to arabicas page containing links to all quality reports 
coffees = driver.find_element_by_xpath('//html/body/header/nav[@id="main"]/div[@class="container"]/div[@class="in"]/a[@href="/coffees"]').click()
time.sleep(3)
driver.find_element_by_link_text('Arabica Coffees').click()
time.sleep(3)

# these values can be changed if this breaks midway through collecting data to pick up close to where you left off
page = 0
coffeenum = 0

# We have 2 pages of data, the first one with 50 rows and the second one with 45 rows
# 8 columns per table, so 50 * 8 = 400 cells max per page
cells = 400

while True:
	print('page {}'.format(page))
	n = 0 # multiple to don't consider the cell

	# 50 rows in these tables * 7 columns per row = 350 cells. Every 7th cell clicks through to that coffee's data page
	for i in range(cells):
		# filter the csv we don't need
		if (i % 8 == 0 and i != 0):
			n += 1

		skips = [0+8*n, 2+8*n, 3+8*n, 5+8*n, 6+8*n, 7+8*n]
		if i in skips:
			print('skipping {}'.format(i))
			pass
		else:

			time.sleep(4)

			# paginate back to the desired page number
			# don't think there's a way around this - the back() option goes too far back
			# some page numbers aren't available in the ui, but 'next' always is unless you've reached the end 
			for p_num in range(page):
				page_buttons = driver.find_elements_by_class_name('paginate_button ')
				page_buttons[-1].click() # the 'next' button
				
				time.sleep(1)
				page_buttons = driver.find_elements_by_class_name('paginate_button ')

			# select the cell to click through to the next coffee-data page
			time.sleep(4) # this next line errors out sometimes, maybe it needs more of a time buffer 
			test_page = driver.find_elements_by_xpath('//td')[i].click()
			time.sleep(2)

			# print('rows: ')
			# print(len(driver.find_elements_by_xpath("//tr")))
			tables = driver.find_elements(By.TAG_NAME, "table")

			# loop over all coffee reports on the page, processing each one and writing to csv
			# print('tables: ')
			# print(len(tables))
			j = 0
			for tab in tables:
				try:
					t = BeautifulSoup(tab.get_attribute('outerHTML'), "html.parser")
					#print(t)
					df = pd.read_html(str(t))
					name = 'coffee_{}_table_{}.csv'.format(coffeenum,j)
					df[0].to_csv(name)
					print(name)
				except:
					# only one's needed but I want this to be onoxious since it's the only way I'm logging this currently
					print('ERROR: {} failed'.format(name))
					print('ERROR: {} failed'.format(name))
					print('ERROR: {} failed'.format(name))
					print('ERROR: {} failed'.format(name))
				j += 1

			# go back to page with all other coffee results
			# driver.back() # note: this isn't working as expected, manually going back to pg 1 via url instead
			driver.get('https://database.coffeeinstitute.org/coffees/arabica')
			time.sleep(2)

		coffeenum += 1

	page += 1
	if page == 2:
		break

# close the driver
driver.close()