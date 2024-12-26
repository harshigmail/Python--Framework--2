import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# static dropdowns
staticdropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
staticdropdown.select_by_index(0)
staticdropdown.select_by_visible_text("Female")


# Dynamic dropdowns
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("Aust")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "Austria":
        country.click()
        break


# break is used because what if in first iteration only found the element why ywe have to iterate all so once it found will exit the loop

# to see which text is present on the field , useful when dynamic dropdowns are present
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
# validate as well
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Austria"

time.sleep(5)