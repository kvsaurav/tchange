
import time
import hashlib
from urllib.request import urlopen, Request
from time import sleep
from selenium import webdriver
import datetime


a = "https://news.ycombinator.com/news"
#a = input("Enter the URL to take screenshot--:\n") #Taking input from the user


# setting the URL you want to monitor
url = Request(a,
			headers={'User-Agent': 'Mozilla/5.0'})



##banner 
def banner():
	print("\t..............................................-------------------------------------------------------------------------------")
	print ("Welcome to T-change")
	cs_banner = """


			    ███      ▄████████    ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄     ▄████████ 
			▀█████████▄ ███    ███   ███    ███     ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ 
			   ▀███▀▀██ ███    █▀    ███    ███     ███    ███ ███   ███   ███    █▀    ███    █▀  
			    ███   ▀ ███         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███         ▄███▄▄▄     
			    ███     ███        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     
 			    ███     ███    █▄    ███    ███     ███    ███ ███   ███   ███    ███   ███    █▄  
			    ███     ███    ███   ███    ███     ███    ███ ███   ███   ███    ███   ███    ███ 
			   ▄████▀   ████████▀    ███    █▀      ███    █▀   ▀█   █▀    ████████▀    ██████████ 
                                                                                       
                                                                                       

            ====================================================================================================================                                           
                                                                                       
                                                          -@4w4r44                             

		"This script will track changes on the URL and if there are any new post or changes it will take screenshot."
	   	 Authored by: @4w4r44 
	    



	 """
	print(cs_banner)
	print("\t---------------------------------------------------------------------------------------------------------------------------")

banner()



def capture():

	driver = webdriver.Chrome(executable_path=r"/home/lab/git/AutomateScreenshot/chromedriver") #add the path of your chromium headless browser. 
	driver.get(a)

	#Giving the file name of screenshot
	date_stamp = str(datetime.datetime.now()).split('.')[0]
	date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
	file_name = date_stamp + ".png"
	driver.save_screenshot(file_name)

	driver.close() #closing the headless broweser.




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
			print("Something has changed in the URL")
			response = urlopen(url).read()
			capture()
			currentHash = hashlib.sha224(response).hexdigest()
			time.sleep(20)
			continue
			
	# To handle exceptions
	except Exception as e:
		print("ERROR")

