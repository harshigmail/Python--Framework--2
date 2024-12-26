import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()
# this will give the window names of all the windows opened
WindowsOpened = driver.window_handles # the present window will be the first and it has index 0
# this will help to switch to preferred window
driver.switch_to.window(WindowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()  #to close the child window 
driver.switch_to.window(WindowsOpened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

