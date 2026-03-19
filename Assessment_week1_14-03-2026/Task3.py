# Description

# Problem Statement:
# Write a Selenium script that opens multiple websites sequentially, including a few e-commerce sites [souled store, nike... any], a news website, and the official Python website. The script should wait for 3 seconds before opening and later should print the title of each page. finally close the browser.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

websites = [
    "https://www.adidas.co.in/",
    "https://www.nike.com/",
    "https://www.amazon.in/",
    "https://www.miumiu.com/",
    "https://gullylabs.com/"
]

for site in websites:
    time.sleep(3)
    driver.get(site)
    print("Website:", site)
    print("Page Title:", driver.title)



driver.quit()