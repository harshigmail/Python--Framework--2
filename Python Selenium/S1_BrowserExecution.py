import time

from selenium import webdriver

# Chrome
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)

# Firefox
driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()

# Edge
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()