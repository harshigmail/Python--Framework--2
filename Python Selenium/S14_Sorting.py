import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

Listitems1 = []
# driver.find_element(By.XPATH, "//span[text() ='Veg/fruit name']")
driver.find_element(By.XPATH,"//tr/th[1]").click()
time.sleep(5)
Listitems = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
for item in Listitems:
    Listitems1.append(item.text)

print(Listitems1)
originalList = Listitems1.copy()
Listitems1.sort()
assert originalList == Listitems1