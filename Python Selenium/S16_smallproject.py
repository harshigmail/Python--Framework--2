import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()


driver.find_element(By.LINK_TEXT, "Shop").click()
time.sleep(5)
phones = driver.find_elements(By.XPATH, "//h4/a")
for phone in phones:
    item = phone.text
    if item == "Nokia Edge":
        phone.find_element(By.XPATH, "//div/button[@class = 'btn btn-info']").click()

driver.find_element(By.CSS_SELECTOR, "a[class*= 'btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*= 'btn-success']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".validate").send_keys("Ind")
# time.sleep(5)
wait = WebDriverWait(driver, 10) # Explicit wait overrides the Implicit wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
countries = driver.find_elements(By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
for country in countries:
    if country.text == 'India':
        country.click()
        break

driver.find_element(By.CSS_SELECTOR, ".validate").get_attribute("value")
driver.find_element(By.XPATH, "//input[@value = 'Purchase']").click()
print(driver.find_element(By.CSS_SELECTOR, ".alert").text)

 # or

SuccessText = driver.find_element(By.CSS_SELECTOR, ".alert").text
assert "Success! Thank you!" in SuccessText
driver.close()










