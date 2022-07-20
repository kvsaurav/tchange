#python3 
# automating screenshot using python selenium module. 
from time import sleep
from selenium import webdriver
import datetime


a = "https://news.ycombinator.com/news"
#a = input("Enter the URL to take screenshot--:\n") #Taking input from the user


def capture():

	driver = webdriver.Chrome(executable_path=r"/home/lab/git/AutomateScreenshot/chromedriver") #add the path of your chromium headless browser. 
	driver.get(a)

	#Giving the file name of screenshot
	date_stamp = str(datetime.datetime.now()).split('.')[0]
	date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
	file_name = date_stamp + ".png"
	driver.save_screenshot(file_name)

	driver.close() #closing the headless broweser.

capture()
