import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Hide and show
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


# Alert popups
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Ram2")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(5)