import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

actualList = []
driver = webdriver.Chrome()
driver.implicitly_wait(5)  # Implicit wait is used insted of using time.sleep everywhere so implicit wait will wiat for provided seconds in each line until the element is found
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type = 'search']").send_keys("ber")
time.sleep(3)
ExpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
Items = driver.find_elements(By.XPATH, "//div[@class = 'products']/div") # Implicit wait won't work here
count = len(Items)
assert count > 0
for item in Items:
    actualList.append(item.find_element(By.XPATH, "h4[@class = 'product-name']").text)
    item.find_element(By.XPATH, "div[3]/button").click()
    # time.sleep(2)
assert actualList == ExpectedList

driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
# time.sleep(4)

# Sum validation
itemamounts = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p[@class = 'amount']" )
sum = 0
for amount in itemamounts:
    print(int(amount.text))
    sum = sum + int(amount.text)   # amount.text grabbed str not int so need to convert

print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalamount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5)
# EW is used when you are sure about that the below element takes more than 5 seconds
wait = WebDriverWait(driver, 10) # Explicit wait overrides the Implicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

totalamount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discountamount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discountamount < totalamount


