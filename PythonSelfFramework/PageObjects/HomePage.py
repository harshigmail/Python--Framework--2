from selenium.webdriver.common.by import By

from PythonSelfFramework.PageObjects.CheckoutPage import CheckOutPage


# self.driver.find_element(By.LINK_TEXT, "Shop").click()
# successmessage = driver.find_element(By.CLASS_NAME, "alert-success").text
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radiobutton = (By.CSS_SELECTOR, "input[id = 'inlineRadio1']")
    name = (By.CSS_SELECTOR, "input[name='name'] ")
    submit = (By.XPATH, "//input[@type='submit'] ")
    alert = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def emails(self):
        return self.driver.find_element(*HomePage.email)

    def passwords(self):
        return self.driver.find_element(*HomePage.password)

    def checkboxes(self):
        return self.driver.find_element(*HomePage.checkbox)

    def radiobuttons(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def names(self):
        return self.driver.find_element(*HomePage.name)

    def submits(self):
        return self.driver.find_element(*HomePage.submit)

    def alerts(self):
        return self.driver.find_element(*HomePage.alert)
