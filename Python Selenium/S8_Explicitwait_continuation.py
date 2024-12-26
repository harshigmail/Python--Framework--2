import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)  # Implicit wait is used insted of using time.sleep everywhere so implicit wait will wiat for provided seconds in each line until the element is found
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type = 'search']").send_keys("ber")
time.sleep(3)
Items = driver.find_elements(By.XPATH, "//div[@class = 'products']/div") # Implicit wait won't work here
count = len(Items)
assert count > 0
for item in Items:
    item.find_element(By.XPATH, "div[3]/button").click()
    # time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
# time.sleep(4)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5)
# EW is used when you are sure about that the below element takes more than 5 seconds
wait = WebDriverWait(driver, 10) # Explicit wait overrides the Implicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

