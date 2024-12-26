import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# print(driver.title)
# print(driver.current_url)

# using ID, CSSSelector, xpath, classname, name, linkText -- identify the element on the UI
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password12")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[id = 'inlineRadio1']").click()

# to write CSS Selector = tagname[attribute = 'value']
driver.find_element(By.CSS_SELECTOR, "input[name='name'] ").send_keys("Ram")

# to write xpath = //tagname[@attribute = 'value']
driver.find_element(By.XPATH, "//input[@type='submit'] ").click()
successmessage = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successmessage)

# if there are more elements with same locator them count your element from top left and add it
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Good")

# to clear
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()


# Validate the messsage
assert "Success!" in successmessage

time.sleep(5)
