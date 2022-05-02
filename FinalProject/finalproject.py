#### This program scrapes indeed.com page and gives our result as a
#### list of all the job_profiles which are currently present there.

from bs4 import BeautifulSoup #To use beutifulsoup to pick elements from html
from selenium import webdriver #To get chrome running on the background
import time #To call sleep funtion to give the webpage enough time to load
import pandas as pd #To export listings variables as excel file
import csv #To convert data to csv

#url of the page we want to scrape
url = input("Please enter the indeed.com URL you want to scrape\n > \n >")

# initiating the webdriver. Path is the path to the chromedriver you have downloaded
driver = webdriver.Chrome(executable_path=r"C:\Users\rames\Desktop\Python\projects\chromedriver.exe")
driver.get(url)

# this is just to ensure that the page is loaded completely
time.sleep(5)

# this renders the JS code and stores all
# of the information in static HTML code.
html = driver.page_source

# Applying bs4 to html variable; html.parser parses text files formatted in HTML
soup = BeautifulSoup(html, "html.parser")

#Pick out job title and print it
jobtitle = soup.find('div',{'class':'jobsearch-JobInfoHeader-title-container'})
print("\nJOB TITLE: ", jobtitle.text)

#Pick out Company Name and print it
companynameAll = soup.find('div',{'class':'jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating'})
#print ("Without splitting reviews: " ,companynameAll.text)
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
    companylocation=companylocation.text.split(word)[1]
    print("LOCATION: " , companylocation)
else:
    companylocation = companylocation.text.split(companyname)[1]
    print("LOCATION: ", companylocation )  

#Print Salary
salary = soup.find('span',{'class':'icl-u-xs-mr--xs'})
if salary is not None:
    salary=salary.text
    print ("SALARY: ", salary)
else:
    salary = "None"
    print (".......NO SALARY TO DISPLAY......")
#Print Job Description
jobdesc = soup.find('div',{'id':'jobDescriptionText'})
#print ("\nJOB DESCRIPTION\n" ,jobdesc.text)

#Print Benefits
benefits=soup.find('div',{'class':'mpci-k3ey05 eu4oa1w0'})
if benefits is not None:
    benefits=benefits.getText(separator=' | ')
    print (f"\nBENEFITS: {benefits}")
else:
    benefits = "None"
    print ("\n....NO BENEFITS HERE....MOVE ALONG.......\n")

driver.close() # closing the webdriver

########################CREATING CSV FILE WITH THE INFORMATION #############################

data = {'Company': [companynameFinal], 'Location':[companylocation], 'Salary': [salary], 'Benefits': [benefits]}
df = pd.DataFrame(data, columns = ['Company', 'Location', 'Salary', 'Benefits'])
df=df.to_csv(r'C:\Users\rames\Desktop\Python\projects\jobs.csv', mode='a', index=False, header=None)

#set criteria to apply, if it meets criteria then put output to csv
#set adblock off and see if it causes problems
#put output to csv
#maybe figure out how to do easy apply automatically



#######################To display = through the screen #################################

#import os

# get the width ("columns") of the screen
#size = os.get_terminal_size()

#print(size)

# convert object to list
#sizelist= list(size)

#print(sizelist)

# element 0 is the width in columns; multiply times whatever
# character (=,*,&,etc.) to fill the width of the screen!
#print("=" * sizelist[0])

#########################################################################################