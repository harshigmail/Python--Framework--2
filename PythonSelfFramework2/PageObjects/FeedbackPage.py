from selenium.webdriver.common.by import By


# driver.find_element(By.ID, "feedback-sf").click()
# driver.find_element(By.XPATH, "//div[@id = 'about_container']//input").send_keys("San")
# user_names = driver.find_elements(By.XPATH, "//ul[@id='select2-about-results']//li")
# driver.find_element(By.XPATH, "//textarea[@class = 'expanding form-control']").send_keys("Add Goals for this year 2024")
# Radiobuttons = driver.find_elements(By.XPATH, "//div[@id='feedback_types']//div/label")
# driver.find_element(By.XPATH, "//div[@id = 'category_container']//li/input[@class = 'select2-search__field']").click()
# Categories = driver.find_elements(By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/span[@class = 'text-dark']")
# attach_button = (driver.find_element(By.XPATH, "//input[@id = 'file']"))
# driver.find_element(By.ID, "submitFeedback").click()
# toaster_locator = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
# Attachment = (By.XPATH, "//ul[@class = 'files-uploaded list-group']")
#  print(driver.find_element(*Attachment).text)
class FeedbackPage:
    def __init__(self, driver):
        self.driver = driver

    Module = (By.ID, "feedback-sf")
    About = (By.XPATH, "//div[@id = 'about_container']//input")
    UserNames = (By.XPATH, "//ul[@id='select2-about-results']//li")
    Textfield = (By.XPATH, "//textarea[@class = 'expanding form-control']")
    Radiobutton = (By.XPATH, "//div[@id='feedback_types']//div/label")
    CategoryClick = (By.XPATH, "//div[@id = 'category_container']//li/input[@class = 'select2-search__field']")
    CategoriesList = (By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/span[@class = 'text-dark']")
    AttachBtn = (By.XPATH, "//input[@id = 'file']")
    Submit = (By.ID, "submitFeedback")
    Toaster = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
    attachment = (By.XPATH, "//ul[@class = 'files-uploaded list-group']")

    def ModuleClick(self):
        return self.driver.find_element(*FeedbackPage.Module)

    def AboutName(self):
        return self.driver.find_element(*FeedbackPage.About)

    def User_Names(self):
        return self.driver.find_elements(*FeedbackPage.UserNames)

    def Text_field(self):
        return self.driver.find_element(*FeedbackPage.Textfield)

    def Radio_Buttons(self):
        return self.driver.find_elements(*FeedbackPage.Radiobutton)

    def Category_Click(self):
        return self.driver.find_element(*FeedbackPage.CategoryClick)

    def Categories_List(self):
        return self.driver.find_elements(*FeedbackPage.CategoriesList)

    def Attach_Button(self):
        return self.driver.find_element(*FeedbackPage.AttachBtn)

    def Submit_Click(self):
        return self.driver.find_element(*FeedbackPage.Submit)

    def attachment_text(self):
        return self.driver.find_element(*FeedbackPage.attachment)

    def toaster_text(self):
        return self.driver.find_element(*FeedbackPage.Toaster)
