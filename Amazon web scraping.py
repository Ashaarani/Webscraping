#!/usr/bin/env python
# coding: utf-8

# In[56]:


get_ipython().system('pip install bs4')
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd


# In[57]:


get_ipython().system('pip install selenium')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[58]:


# Set up the Safari WebDriver
driver = webdriver.Safari()

#connect to website
    
URL='https://www.amazon.com/funny-analyst-definition-scientist-t-shirt/dp/B07NLP2PKY/ref=sr_1_4?crid=IYUM6BNZOA9I&dib=eyJ2IjoiMSJ9.PM2zhQFx_lfPnddZwr05DvJ8zxTiKbMNof3H_8ObTes8YarT96m4jiSWTM-p0IE3bA2qY9UPmB77hgju1FjQdzoGTg9Z9RCoiq9k-QHkViQOvTyZAA-_97_tVX9KJmI4FEwuFkUjYmo-JXkjcqp2P6u3dh89brhiDetURS8hTpn4R6oUt6SHbBSapqx2Ln-bx-5Ccuee5XhzWDSZZwnwtMfCQIB3vQMZNUs78e62AeIJ1v9NvvOPsnKMAe2SQWdOD-kBkATixwK7JUzEV_4SNMW3msbHZV0_rQ7BBZ6e4iw.r0fDge_RYbaEYjv4seJoPU6BZ5ChEhC6rfg9GFD2TzE&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1721596729&sprefix=data%2Banalyst%2B%2Caps%2C95&sr=8-4'

driver.get(URL)


#print(soup1)


# In[59]:


# Get the page content
page_content = driver.page_source

# Close the WebDriver
driver.quit()

# Use BeautifulSoup to parse the page content
soup1 = BeautifulSoup(page_content, 'html.parser')


# In[60]:


soup2= BeautifulSoup(soup1.prettify(),'html.parser')
print(soup2)


# In[61]:


title= soup2.find(id='productTitle').get_text().strip() 

print(title)


# In[62]:


price= soup2.find(id='corePriceDisplay_desktop_feature_div').get_text().strip().split('\n')[0][1:]


print(price)


# In[63]:


today= datetime.date.today()
print(today)


# In[64]:


# Create CSV and write headers and data into the file

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('/Users/asharani/Desktop/Study material/AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[65]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[66]:


#Combine all of the above code into one function


def check_price():
    driver = webdriver.Safari()
    URL = 'https://www.amazon.com/funny-analyst-definition-scientist-t-shirt/dp/B07NLP2PKY/ref=sr_1_4?crid=IYUM6BNZOA9I&dib=eyJ2IjoiMSJ9.PM2zhQFx_lfPnddZwr05DvJ8zxTiKbMNof3H_8ObTes8YarT96m4jiSWTM-p0IE3bA2qY9UPmB77hgju1FjQdzoGTg9Z9RCoiq9k-QHkViQOvTyZAA-_97_tVX9KJmI4FEwuFkUjYmo-JXkjcqp2P6u3dh89brhiDetURS8hTpn4R6oUt6SHbBSapqx2Ln-bx-5Ccuee5XhzWDSZZwnwtMfCQIB3vQMZNUs78e62AeIJ1v9NvvOPsnKMAe2SQWdOD-kBkATixwK7JUzEV_4SNMW3msbHZV0_rQ7BBZ6e4iw.r0fDge_RYbaEYjv4seJoPU6BZ5ChEhC6rfg9GFD2TzE&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1721596729&sprefix=data%2Banalyst%2B%2Caps%2C95&sr=8-4'
    driver.get(URL)
    page_content = driver.page_source
    driver.quit()

    soup1 = BeautifulSoup(page_content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title= soup2.find(id='productTitle').get_text().strip() 

    price= soup2.find(id='corePriceDisplay_desktop_feature_div').get_text().strip().split('\n')[0][1:]
    
    today= datetime.date.today()
    
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[67]:


while(True):
    check_price()
    time.sleep(3600)


# In[68]:


df = pd.read_csv('/Users/asharani/Desktop/Study material/AmazonWebScraperDataset.csv')

print(df)


# In[69]:









