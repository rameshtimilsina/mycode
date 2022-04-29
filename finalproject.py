#### This program scrapes indeed.com page and gives our result as a
#### list of all the job_profiles which are currently present there.

#import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

#url of the page we want to scrape
url = input("Please enter the Indeed URL you want to scrape\n > \n >")

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome(executable_path=r"C:\Users\rames\Desktop\Python\projects\chromedriver.exe")
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

# this renders the JS code and stores all
# of the information in static HTML code.
html = driver.page_source

# Applying bs4 to html variable
soup = BeautifulSoup(html, "html.parser")

#Pick out job title and print it
jobtitle = soup.find('div',{'class':'jobsearch-JobInfoHeader-title-container'})
print("\nJOB TITLE: ", jobtitle.text)

#Pick out Company Name and print it
companynameAll = soup.find('div',{'class':'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'})
companyname=companynameAll.getText(separator=' ')

#splitting string using reviews as key and getting everything prior to the key 
companyname=companyname.split("reviews")[0]

#replacing all the numerical characters from name
companynameFinal=''.join(map(lambda c:'' if c in '0123456789' else c,companyname))
#printing name while replacing ',' that was getting output at the end of the companyname
print("COMPANY NAME: ", companynameFinal.replace(',',''))


#Pick out location and print it
companylocation = soup.find('div',{'class':'jobsearch-CompanyInfoContainer'})
word="reviews"
if word in companylocation.text:
    print("LOCATION: " , companylocation.text.split(word)[1])
else:
    print("LOCATION: ", companylocation.text.split(companyname)[1])  

#Print Salary
salary = soup.find('span',{'class':'icl-u-xs-mr--xs'})
print ("SALARY: ", salary.text)

#Print Job Description
jobdesc = soup.find('div',{'id':'jobDescriptionText'})
#print ("\nJOB DESCRIPTION\n" ,jobdesc.text)

#Print Benefits
benefits=soup.find('div',{'class':'mpci-k3ey05 eu4oa1w0'})
if benefits is not None:
    print ("\nBENEFITS: ", benefits.getText(separator=' '))
else:
    print ("\n....NO BENEFITS HERE....MOVE ALONG.......\n")

driver.close() # closing the webdriver
