import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


# we can use the click method but the problem is that we are not sure whether that options will be there in that position only so we can use the below method
Radiobuttons = driver.find_elements(By.XPATH, "//input[@type = 'radio']")
print(len(Radiobuttons))

for radiobutton in Radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        print(radiobutton.is_selected())
        # assert radiobutton.is_selected()
        break


time.sleep(2)
