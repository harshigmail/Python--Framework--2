import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# ------------------Headless mode
chrome_options.add_argument("headless")
# ----------------ignore certification error - selenium will take care such errors
chrome_options.add_argument("--ignore-certification-errors")
# --------------------maximize the window
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

