from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib2 import urlopen
from urllib import quote_plus
#from db import Review
from datetime import date
import time
import re
import csv

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')

csv_file = open('carsdata4.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)

url_file = open('carvana_urls.csv')
url_list = url_file.readlines()
url_file.close()

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument('headless')
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
#chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


counter = 0
errorcounter = 0

for x in url_list[1:15000]:
	
	y = 'https://api.scraperapi.com/?key=c870e563e8020c65b2fce5cf21a79e5f&url='+x+'&render=True'
	request_token = 'nGyVBP_Z4Yppr7qJlMBY_w'

	url = quote_plus('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Boston,+MA')

	handler = urlopen('https://api.proxycrawl.com/?token=rMbbg4YXcd0KVviqBbdWXw&format=json&url=' + url)



	driver.get(x)
	try:
		time.sleep(10) 
		#sold_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									#'//div[@class="modal-btn-close"]')[-1]))
		sold_button = driver.find_elements_by_xpath('//div[@class="modal-btn-close"]')[-1]
		print("popup at",x)
		# time.sleep(5)
		#//*[@id="viewporter-wrapper"]/div[3]/div/div/vdp-availability-subscription-modal/div/div[2]
		sold_button.click()
		print('======= pop up closed ==========')
		# driver.switchTo().alert().dismiss()
	except:
		print("no popup at",x)
	try:	
		#driver.execute_script('window.open(x)')
		#Path Definition
		testpath = '//div[@ng-bind-html="feature.value"]'
		yearpath = '//span[@class="vdp-header-title-minor"]'
		makepath = '//span[@class="vdp-header-title-main"]'
		mileagepath = '//div[@class="vdp-header-subtitle-minor"]'
		hwypath = '//div[@class="vdp-summary-hwy-mpg"]'
		citypath = '//div[@class="vdp-summary-city-mpg"]'
		pricepath = '//span[@data-cv-test="Cv.Vdp.Price"]'
		#Price path <span class="vdp-header-pricing-amount" data-cv-test="Cv.Vdp.Price" ng-class="{'vdp-header-discounted-pricing-amount':vm.details.vehicle.pricing.isPriceDiscounted}"> $13,600 </span>
		bodypath = '//*[@id="vdp-the-basics"]/dl/dd[1]/div/div'
		passengerpath = '//*[@id="vdp-the-basics"]/dl/dd[2]/div/div' 
		exteriorpath = '//*[@id="vdp-the-basics"]/dl/dd[3]/div/div'
		interiorpath = '//*[@id="vdp-the-basics"]/dl/dd[4]/div/div'
		wheelpath = '//*[@id="vdp-the-basics"]/dl/dd[5]/div/div'
		tirepath = '//*[@id="vdp-the-basics"]/dl/dd[6]/div/div'
		fuelpath = '//*[@id="vdp-the-basics"]/dl/dd[7]/div/div'
		basicpath =  '//*[@id="vdp-the-basics"]/dl/dd[8]/div/div'
		powerpath = '//*[@id="vdp-the-basics"]/dl/dd[9]/div/div'
		enginepath = '//*[@id="vdp-the-basics"]/dl/dd[10]/div/div'
		horsepath = '//*[@id="vdp-the-basics"]/dl/dd[11]/div/div'
		transpath = '//*[@id="vdp-the-basics"]/dl/dd[12]/div/div'
		stockpath = '//*[@id="vdp-the-basics"]/dl/dd[13]/div/div'
		vinpath = '//*[@id="vdp-the-basics"]/dl/dd[14]/div/div'
		#passenger

		time.sleep(7)

		#cartest = driver.find_elements_by_xpath(testpath)  #list of everything in the table
		try:
			yeartest = driver.find_element_by_xpath(yearpath).text
		except:
			yeartest = 'NA'

		try:
			maketest = driver.find_element_by_xpath(makepath).text
		except:
			maketest = 'NA'

		try:
			mileagetest = driver.find_element_by_xpath(mileagepath).text
		except:
			mileagetest = 'NA'

		try:	
			hwytest = driver.find_element_by_xpath(hwypath).text
		except:
			hwytest = 'NA'

		try:	
			citytest = driver.find_element_by_xpath(citypath).text
		except:
			citytest = 'NA'

		try:			
			pricetest = driver.find_element_by_xpath(pricepath).text
		except:
			pricetest = 'NA'

		try:		
			bodytest = driver.find_element_by_xpath(bodypath).text
		except:
			bodytest = 'NA'

		try:	
			passengertest = driver.find_element_by_xpath(passengerpath).text
		except:
			passengertest = 'NA'

		try:	
			exteriortest = driver.find_element_by_xpath(exteriorpath).text
		except:
			exteriortest = 'NA'

		try:
			interiortest = driver.find_element_by_xpath(interiorpath).text
		except:
			interiortest = 'NA'
		
		try:
			wheeltest = driver.find_element_by_xpath(wheelpath).text
		except:
			wheeltest = 'NA'
		
		try:
			tiretest = driver.find_element_by_xpath(tirepath).text
		except:
			tiretest = 'NA'

		try:	
			fueltest = driver.find_element_by_xpath(fuelpath).text
		except:
			fueltest = 'NA'
		
		try:	
			basictest = driver.find_element_by_xpath(basicpath).text
		except:
			basictest = 'NA'
		
		try:
			powertest = driver.find_element_by_xpath(powerpath).text
		except:
			powertest = 'NA'
		
		try:
			enginetest = driver.find_element_by_xpath(enginepath).text
		except:
			enginetest = 'NA'
		
		try:
			horsetest = driver.find_element_by_xpath(horsepath).text
		except:
			horsetest = 'NA'
		
		try:
			transtest = driver.find_element_by_xpath(transpath).text
		except:
			transtest = 'NA'

		try:	
			stocktest = driver.find_element_by_xpath(stockpath).text
		except:
			stocktest = 'NA'

		try:
			vintest = driver.find_element_by_xpath(vinpath).text
		except: 
			vintest = 'NA'


		

		cardict = {}
		counter = counter + 1
		print(counter)
		
		#while index<2:
		#	try:
				#print("Year:"+str(yeartest))
				#print("Make:"+str(maketest))
				#print("Mileage:"+str(mileagetest))
				#print("Highway MPG:"+str(hwytest))
				#print("City MPG:"+str(citytest))
				#print("Price:"+str(pricetest))
				#index = index + 1
				# Find all the reviews on the page
				#wait_cardetails = WebDriverWait(driver, 10)
				#cardetails = wait_cardetails.until(EC.presence_of_all_elements_located((By.XPATH,
											#'//div[@class="vdp-the-basics-basics-value" ng-bind-html="feature.value" ng-if="feature.display !== \'VIN\'"]')))
		
				#<div class="vdp-the-basics-basics-value" ng-bind-html="feature.value" ng-if="feature.display !== 'VIN'">5</div>
		cardict['url'] = x
		cardict['body'] = bodytest
		cardict['passenger'] = passengertest
		cardict['exterior'] = exteriortest
		cardict['interior'] = interiortest
		cardict['wheel'] = wheeltest
		cardict['tire'] = tiretest
		cardict['fuel'] = fueltest
		cardict['basic'] = basictest
		cardict['powertrain'] = powertest
		cardict['engine'] = enginetest
		cardict['horsepower'] = horsetest
		cardict['transmission'] = transtest
		cardict['stocknumber'] = stocktest
		cardict['vinnumber'] = vintest
		cardict['year'] = yeartest
		cardict['make'] = maketest
		cardict['mileage'] = mileagetest
		cardict['highway'] = hwytest
		cardict['city'] = citytest
		cardict['price'] = pricetest
		print(cardict)

		
		writer.writerow(cardict.values())
		
		
	except Exception as e:
		errorcounter = errorcounter + 1
		print("Error",errorcounter,x,e)
		next

				# Use relative xpath to locate the title, text, username, date.
				# Once you locate the element, you can use 'element.text' to return its string.
				# To get the attribute instead of the text of each element, use 'element.get_attribute()'
				#title = review.find_element_by_xpath('./').text
				#text = review.find_element_by_xpath('.//span[@itemprop="reviewBody"]').text
				#username = review.find_element_by_xpath('.//span[@itemprop="author"]').text

				# We use date_ to avoid naming conflict with the date method from datetime.
				#date_published = review.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content').split('T')[0]
				#year, month, day = map(lambda x: int(x), date_published.split('-'))
				#date_published = date(year, month, day)

	#	except Exception as e:
	#		print(e)
	#		driver.close()
	#		break



	#GOOGLE:  Pickling / pickle in python  



