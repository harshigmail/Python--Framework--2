from selenium.webdriver.common.by import By


#  self.driver.find_element(By.CSS_SELECTOR, ".validate").send_keys("Ind")
# self.driver.find_elements(By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
# self.driver.find_element(By.CSS_SELECTOR, ".validate").get_attribute("value")
#  self.driver.find_element(By.XPATH, "//input[@value = 'Purchase']").click()
#  print(self.driver.find_element(By.CSS_SELECTOR, ".alert").text)
# self.driver.find_element(By.CSS_SELECTOR, ".alert").text
class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    SelectCountry = (By.CSS_SELECTOR, ".validate")
    ListCountry = (By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
    Validate = (By.CSS_SELECTOR, ".validate")
    Purchase = (By.XPATH, "//input[@value = 'Purchase']")
    Alert = (By.CSS_SELECTOR, ".alert")
    Success = (By.CSS_SELECTOR, ".alert")



    def SelectCountries(self):
        return self.driver.find_element(*ConfirmPage.SelectCountry)

    def ListCountries(self):
        return self.driver.find_elements(*ConfirmPage.ListCountry)

    def Validates(self):
        return self.driver.find_element(*ConfirmPage.Validate)

    def Purchases(self):
        return self.driver.find_element(*ConfirmPage.Purchase)

    def Alerts(self):
        return self.driver.find_element(*ConfirmPage.Alert)

    def Successes(self):
        return self.driver.find_element(*ConfirmPage.Success)