

#will try to take screenshot on any change in the website 

import time
import hashlib
from urllib.request import urlopen, Request

from selenium import webdriver
from time import sleep

link = "https://twitter.com/_r_netsec"

# setting the URL you want to monitor
url = Request(link,
			headers={'User-Agent': 'Mozilla/5.0'})


response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(2)
while True:
	try:
		# perform the get request and store it in a var
		response = urlopen(url).read()
		
		# create a hash
		currentHash = hashlib.sha224(response).hexdigest()
		
		# wait for 5 seconds
		time.sleep(5)
		
		# perform the get request
		response = urlopen(url).read()
		
		# create a new hash
		newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash
		if newHash == currentHash:
			continue

		# if something changed in the hashes
		else:

			# notify
			print("something changed taking a screenshot")


			driver = webdriver.Chrome(executable_path=r"/home/lab/git/AutomateScreenshot/chromedriver") #add the path of your chromium headless browser. 


			#The url that we want to take Screenshot
			driver.get(link)

			#Giving the file name of screenshot
			driver.save_screenshot(r"screenshot.png")

			driver.close() #closing the headless broweser.




			# again read the website
			response = urlopen(url).read()

			# create a hash
			currentHash = hashlib.sha224(response).hexdigest()

			# wait for 30 seconds
			time.sleep(30)
			continue
			
	# To handle exceptions
	except Exception as e:
		print("error")

