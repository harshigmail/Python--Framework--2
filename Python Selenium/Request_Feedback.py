import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
file_path = "C:\\Users\\harshitha.n\\Downloads\\30-Day Employee Performance Review Template.pdf"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://pfsmigrationdata.mastmojo.com/sign_in?")
driver.maximize_window()
driver.find_element(By.NAME, "user[user_name]").send_keys("niranjanmigration@karnab.com")
driver.find_element(By.NAME, "user[password]").send_keys("Niranjanmigration@123")
driver.find_element(By.CLASS_NAME, "signin-btn").click()
wait = WebDriverWait(driver, 10)  # Explicit wait overrides the Implicit wait
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@data-value= 'feedback']")))

driver.get("https://pfsmigrationdata.mastmojo.com/pages/my_corner/feedback#overview")
driver.find_element(By.ID, "feedback-rf").click()


Radiobuttons = driver.find_elements(By.XPATH, "//div[@class = 'form-check form-check-inline']//label")
print(len(Radiobuttons))
for radiobutton in Radiobuttons:
    print(radiobutton.text)
    if radiobutton.text == "Someone":
        radiobutton.click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@id = 'someone-container']/span/span/span[@class = 'select2-selection select2-selection--single']").click()
driver.find_element(By.XPATH, "//div[@id = 'someone-container']/span[2]/span/span/input").send_keys("San")
time.sleep(8)
user_names = driver.find_elements(By.XPATH, "//ul[@id = 'select2-someone-results']/li/div/div[@class = 'select2-title']")
for user in user_names:
    if "Sandyashree Kumar" in user.text:
        user.click()
        break
time.sleep(3)

driver.find_element(By.XPATH, "//div[@id = 'recipient_section']//span/ul/li/input").send_keys("San")
time.sleep(8)
user_names = driver.find_elements(By.XPATH, "//ul[@id = 'select2-to-results']/li/div/div[@class = 'select2-title']")
for user in user_names:
    if "Sanjay Kumar" in user.text:
        user.click()
        break
time.sleep(3)

driver.find_element(By.ID, "request").send_keys("Request feedback- year 2023")


driver.find_element(By.XPATH, "//div[@id = 'categories_section']//li/input[@class = 'select2-search__field']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class, 'select2-results__options')]/li")))
Categories = driver.find_elements(By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/span[@class = 'text-dark']")
print(len(Categories))
for category in Categories:
    if category.get_attribute(
            "title") == "Uses sound judgment to make good decisions based on information gathered and analyzed. Considers all pertinent facts and alternatives before deciding on the most appropriate action. Commits to decision.":
        category.click()
        break
time.sleep(1)

driver.find_element(By.ID, "submitRequest").click()
wait = WebDriverWait(driver, 20)
toaster_locator = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
wait.until(expected_conditions.presence_of_element_located(toaster_locator))
print(driver.find_element(*toaster_locator).text)

