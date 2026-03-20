# Task-2 :-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/signup")
driver.maximize_window()

name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")

name_input.send_keys("Justin Bieber")
email_input.send_keys("connect@jb123.com")

signup_btn = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
signup_btn.click()

wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))

title = wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))
title.click()

newsletter = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")

newsletter.click()
offers.click()

print("Newsletter :", newsletter.get_attribute("checked"))
print("Special offers :", offers.get_attribute("checked"))

driver.quit()
sleep(5)




