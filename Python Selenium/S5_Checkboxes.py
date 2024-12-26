import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1").click()
# driver.find_element(By.CSS_SELECTOR, "#checkBoxOption2").click()

# we can use the above method but the problem is that we are not sure whether that options will be there in that position only so we can use the below method
Checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
print(len(Checkboxes))

for checkbox in Checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        print(checkbox.is_selected())
        # assert checkbox.is_selected()
        break


time.sleep(2)
