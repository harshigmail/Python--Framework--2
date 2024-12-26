from selenium.webdriver.common.by import By

from PythonSelfFramework.PageObjects.ConfirmPage import ConfirmPage


# self.driver.find_elements(By.XPATH, "//h4/a")
# find_element(By.XPATH, "//div/button[@class = 'btn btn-info']")
# self.driver.find_element(By.CSS_SELECTOR, "a[class*= 'btn-primary']").click()
# self.driver.find_element(By.CSS_SELECTOR, "button[class*= 'btn-success']").click()
class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    PhonesTitle = (By.CSS_SELECTOR, ".card-title a")
    Button = (By.XPATH, "//div/button[@class = 'btn btn-info']")
    ChekOutbtn = (By.CSS_SELECTOR, "a[class*= 'btn-primary']")
    Checkout1 = (By.CSS_SELECTOR, "button[class*= 'btn-success']")

    def PhoneItem(self):
        return self.driver.find_elements(*CheckOutPage.PhonesTitle)

    def ButtonAdd(self, phone):
        return phone.find_element(*CheckOutPage.Button)

    def CheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.ChekOutbtn)

    def CheckoutButton1(self):
        self.driver.find_element(*CheckOutPage.Checkout1).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
