import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# write xpath using parent child concept
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("hello@gmail.com")
# write CSS using parent child concept
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys(password4)



time.sleep(3)