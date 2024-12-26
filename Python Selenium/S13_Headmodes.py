import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# ------------------Headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# ----------------ignore certification error - selenium will take care such errors
chrome_options.add_argument("--ignore-certification-errors")

driver = webdriver.Chrome(options = chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# ---------------scroll to bottom
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")



