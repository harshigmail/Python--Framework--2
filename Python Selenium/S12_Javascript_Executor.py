import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# ---------------scroll to bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(3)
# ---------------get screenshot
driver.get_screenshot_as_file("screen.png")

