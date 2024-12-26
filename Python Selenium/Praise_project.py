import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
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
driver.find_element(By.ID, "praise").click()

driver.find_element(By.XPATH, "//li/input[@class = 'select2-search__field']").send_keys("San")
time.sleep(3)
user_names = driver.find_elements(By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/div[2]")
for user in user_names:
    if "Sanjay Kumar" in user.text:
        user.click()
        break
time.sleep(2)

driver.find_element(By.XPATH, "//textarea[@id = 'praise_textbox']").send_keys(" Praise San for last year 2023")

Tags = ["Praise2024", "Praise2023", "Praise2022"]
for Tag in Tags:
    Tag1 = (driver.find_element(By.XPATH, "//li/input[@class = 'tagit-input ui-autocomplete-input']"))
    Tag1.send_keys(Tag)
    Tag1.send_keys(Keys.ENTER)
time.sleep(5)

Public_library = driver.find_elements(By.XPATH, "//ul[@class = 'library-lists nav nav-pills']/li")
print(len(Public_library))
for item in Public_library:
    if "Praise" in item.text:
        item.click()
wait = WebDriverWait(driver, 10)
wait.until(
    expected_conditions.visibility_of_all_elements_located((By.XPATH, "//div[@id = 'images-list-container']/div")))
scrollable_container = driver.find_element(By.ID, "images-list-container")
# Find initially visible elements inside the container
child_elements = scrollable_container.find_elements(By.XPATH, "./div")
# Get the count of visible elements
initial_count = len(child_elements)
# Scroll and load all elements
last_count = 0
while last_count != initial_count:
    last_count = initial_count

    # Scroll to the end of the container
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_container)
    time.sleep(10)  # Wait for new elements to load

    # Count the elements again
    child_elements = scrollable_container.find_elements(By.XPATH, "./div")
    initial_count = len(child_elements)

print(f"Total number of elements: {initial_count}")
for element in child_elements:
    image = element.find_element(By.TAG_NAME, "img")
    if image.get_attribute("src") == "https://cdn.mastmojo.com/engagedly_image_library/Great.png":
        driver.execute_script("arguments[0].scrollIntoView();", image)
        image.click()
        print("Image clicked successfully")
        break
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class = 'mb-1 preview-images']/div/img")))
print("Preview element is visible")
# screenshot of image
driver.get_screenshot_as_file("screenImage.png")

driver.find_element(By.XPATH, "//div[text() = 'My Computer']").click()
time.sleep(3)
browse_button = (driver.find_element(By.XPATH, "//input[@id = 'file']"))
browse_button.send_keys(file_path)
wait = WebDriverWait(driver, 10)
Attachment = (By.CLASS_NAME, "uploaded-img-container")
wait.until(expected_conditions.visibility_of_element_located(Attachment))
print(driver.find_element(*Attachment).text)


driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-primary post-praise']").click()
wait = WebDriverWait(driver, 20)
toaster_locator = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
wait.until(expected_conditions.presence_of_element_located(toaster_locator))
print(driver.find_element(*toaster_locator).text)
