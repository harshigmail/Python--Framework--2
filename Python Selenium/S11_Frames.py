

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

# Frames are embedded html which sits on top of our base html
# switch to frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am good")
# Switch back to default content
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, ".h3").text)
