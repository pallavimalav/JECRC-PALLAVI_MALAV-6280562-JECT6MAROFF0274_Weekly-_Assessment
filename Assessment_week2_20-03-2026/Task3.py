# Task-3 :-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.google.com")

search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("Selenium Python")

suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul[role='listbox'] li")))

print("Suggestions:")
valid_suggestions = []

for i, suggestion in enumerate(suggestions):
    text = suggestion.text
    if text:
        valid_suggestions.append(suggestion)
        print(f"{len(valid_suggestions)}. {text}")

if valid_suggestions:
    valid_suggestions[0].click()

driver.quit()
sleep(5)







