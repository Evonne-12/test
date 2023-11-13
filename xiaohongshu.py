import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
search_word = "非那雄胺"

# Open the Xiaohongshu search page
driver.get(f"https://www.xiaohongshu.com/search_result?keyword={search_word}")
driver.maximize_window()

# Waiting for the page to load (adjust the sleep time as needed)
time.sleep(20)

# Get the page source after waiting
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract title
title_element = soup.find_all('a', class_='title')
if title_element:
 for i in title_element:
    print(i.text.strip())



# Close the webdriver
driver.quit()
