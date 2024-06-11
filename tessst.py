from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

url ="https://www.imdb.com/chart/top/"
headers = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# Set up Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)  

page_source = driver.page_source

# Close the Selenium WebDriver
driver.quit()

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all movie titles
title_elements = soup.findAll('h3', class_='ipc-title__text')
# Find all movie ratings
rating = soup.findAll('span',class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
# Find all year of the movies
year = soup.findAll('span',class_='cli-title-metadata-item')

listt=[]
# Print all movie titles
for title_element,rating_ele,year_ele in zip(title_elements,rating,year):
    title = title_element.get_text(strip=True)
    rating =rating_ele.get_text(strip=True)
    year =year_ele.get_text(strip=True)
    if title[0].isdigit() and len(year) == 4:
        listt.append({"Title":title,'Rating':rating,'year':year})

df =pd.DataFrame(listt)
print(df)
df.to_csv('file1.csv',index=False)