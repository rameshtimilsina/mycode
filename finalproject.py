#!/usr/bin/env python3

import requests
#import webdriver from selenium
from selenium import webdriver

print("\n############### THIS PROGRAM IS DESIGNED TO SCRAPE THE PROVIDED WEBSITE #############")
print("\n#####################################################################################")



URL="https://realpython.github.io/fake-jobs/"
URL.json()
page=requests.get(URL)

#print(page.text)
