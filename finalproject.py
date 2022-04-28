#!/usr/bin/env python3

import requests
#import webdriver from selenium
from selenium import webdriver

print("\n############### THIS PROGRAM IS DESIGNED TO SCRAPE THE PROVIDED WEBSITE #############")
print("\n#####################################################################################")



#URL="https://realpython.github.io/fake-jobs/"
#URL.json()
#page=requests.get(URL)
path='/home/student/mycode/chromedriver_linux64.zip'
driver=webdriver.Chrome(executable_path = path)
driver.get('https://www.linkedin.com/jobs/software-engineer-jobs-tacoma-washington-united-states/?distance=25&geoId=104976816')

print(driver.text)
