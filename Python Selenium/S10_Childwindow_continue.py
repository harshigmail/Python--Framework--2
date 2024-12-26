from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Assignment
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
textData = driver.find_element(By.XPATH, "//div/p[2]").text
username = textData[19:48]
print(username)

driver.switch_to.window(WindowsOpened[0])
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys("password12")
driver.find_element(By.NAME, "signin").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)




