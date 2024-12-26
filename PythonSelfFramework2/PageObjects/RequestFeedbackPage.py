# driver.find_element(By.ID, "feedback-rf").click()
# Radiobuttons = driver.find_elements(By.XPATH, "//div[@class = 'form-check form-check-inline']//label")
# driver.find_element(By.XPATH, "//div[@id = 'someone-container']/span/span/span[@class = 'select2-selection select2-selection--single']").click()
# driver.find_element(By.XPATH, "//div[@id = 'someone-container']/span[2]/span/span/input").send_keys("San")
# user_names = driver.find_elements(By.XPATH, "//ul[@id = 'select2-someone-results']/li/div/div[@class = 'select2-title']")
# driver.find_element(By.XPATH, "//div[@id = 'recipient_section']//span/ul/li/input").send_keys("San")
# driver.find_elements(By.XPATH, "//ul[@id = 'select2-to-results']/li/div/div[@class = 'select2-title']")
# driver.find_element(By.ID, "request").send_keys("Request feedback- year 2023")
# driver.find_element(By.XPATH, "//div[@id = 'categories_section']//li/input[@class = 'select2-search__field']").click()
# Categories = driver.find_elements(By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/span[@class = 'text-dark']")
# driver.find_element(By.ID, "submitRequest").click()
# toaster_locator = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
from selenium.webdriver.common.by import By


class RequestFeedbackPage:
    def __init__(self, driver):
        self.driver = driver

    Module = (By.ID, "feedback-rf")
    RadioButton = (By.XPATH, "//div[@class = 'form-check form-check-inline']//label")
    SomeOne = (
        By.XPATH,
        "//div[@id = 'someone-container']/span/span/span[@class = 'select2-selection select2-selection--single']")
    SomeOneData = (By.XPATH, "//div[@id = 'someone-container']/span[2]/span/span/input")
    UserNames = (By.XPATH, "//ul[@id = 'select2-someone-results']/li/div/div[@class = 'select2-title']")
    From = (By.XPATH, "//div[@id = 'recipient_section']//span/ul/li/input")
    fromUser = (By.XPATH, "//ul[@id = 'select2-to-results']/li/div/div[@class = 'select2-title']")
    Textfield = (By.ID, "request")
    CategoryClick = (By.XPATH, "//div[@id = 'categories_section']//li/input[@class = 'select2-search__field']")
    Categories = (By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/span[@class = 'text-dark']")
    submit = (By.ID, "submitRequest")
    ToasterRequest = (By.XPATH, "//div[@class = 'engagedly-toast-message']")

    def ModuleClick(self):
        return self.driver.find_element(*RequestFeedbackPage.Module)

    def Radio_Buttons(self):
        return self.driver.find_elements(*RequestFeedbackPage.RadioButton)

    def Some_One(self):
        return self.driver.find_element(*RequestFeedbackPage.SomeOne)

    def SomeOne_Data(self):
        return self.driver.find_element(*RequestFeedbackPage.SomeOneData)

    def User_Names(self):
        return self.driver.find_elements(*RequestFeedbackPage.UserNames)

    def From_recepient(self):
        return self.driver.find_element(*RequestFeedbackPage.From)

    def From_User_Names(self):
        return self.driver.find_elements(*RequestFeedbackPage.fromUser)

    def Text_Field(self):
        return self.driver.find_element(*RequestFeedbackPage.Textfield)

    def Category_click(self):
        return self.driver.find_element(*RequestFeedbackPage.CategoryClick)

    def Categories_List(self):
        return self.driver.find_elements(*RequestFeedbackPage.Categories)

    def Submit_btn(self):
        return self.driver.find_element(*RequestFeedbackPage.submit)

