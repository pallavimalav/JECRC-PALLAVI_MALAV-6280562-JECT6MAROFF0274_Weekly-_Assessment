# Task-1 :-

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

driver.get("https://www.amazon.in")
driver.maximize_window()

print("Title:", driver.title)
print("URL:", driver.current_url)

submit = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="a-button-inner"]')))
submit.click()

dropdown_button = wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))

select = Select(dropdown_button)
select.select_by_visible_text("Books")

search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

search_bar.send_keys("Harry Potter")
search_bar.send_keys(Keys.ENTER)

products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']//h2//span")))
print("\nFirst 5 Products:")
for i in products[:5]:
    print(i.text)

products[0].click()

driver.quit()
sleep(5)



