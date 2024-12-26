# driver.find_element(By.ID, "praise").click()
# driver.find_element(By.XPATH, "//li/input[@class = 'select2-search__field']").send_keys("San")
# user_names = driver.find_elements(By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/div[2]")
# driver.find_element(By.XPATH, "//textarea[@id = 'praise_textbox']").send_keys(" Praise San for last year 2023")
#  Tag1 = (driver.find_element(By.XPATH, "//li/input[@class = 'tagit-input ui-autocomplete-input']"))
# Public_library = driver.find_elements(By.XPATH, "//ul[@class = 'library-lists nav nav-pills']/li")
# scrollable_container = driver.find_element(By.ID, "images-list-container")
# driver.find_element(By.XPATH, "//div[text() = 'My Computer']").click()
# browse_button = (driver.find_element(By.XPATH, "//input[@id = 'file']"))
# (By.CLASS_NAME, "uploaded-img-container")
# driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-primary post-praise']").click()
# toaster_locator = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_container)
from selenium.webdriver.common.by import By


class PraisePage:
    def __init__(self, driver):
        self.driver = driver

    Module = (By.ID, "praise")
    About = (By.XPATH, "//li/input[@class = 'select2-search__field']")
    UserNames = (By.XPATH, "//ul[@class = 'select2-results__options eng-scroll-sm']/li/div[2]")
    Textfield = (By.XPATH, "//textarea[@id = 'praise_textbox']")
    Tag = (By.XPATH, "//li/input[@class = 'tagit-input ui-autocomplete-input']")
    PublicLibrary = (By.XPATH, "//ul[@class = 'library-lists nav nav-pills']/li")
    scroll = (By.ID, "images-list-container")
    MyComputer = (By.XPATH, "//div[text() = 'My Computer']")
    browse = (By.XPATH, "//input[@id = 'file']")
    AttachmentPraise = (By.CLASS_NAME, "uploaded-img-container")
    PraiseBtn = (By.CSS_SELECTOR, "button[class = 'btn btn-primary post-praise']")
    toasterPraise = (By.XPATH, "//div[@class = 'engagedly-toast-message']")
    Tags = ["Praise2024", "Praise2023", "Praise2022"]


    def ModuleClick(self):
        return self.driver.find_element(*PraisePage.Module)

    def AboutName(self):
        return self.driver.find_element(*PraisePage.About)

    def User_Names(self):
        return self.driver.find_elements(*PraisePage.UserNames)

    def Text_field(self):
        return self.driver.find_element(*PraisePage.Textfield)

    def Tag_assign(self):
        return self.driver.find_element(*PraisePage.Tag)

    def Public_Library(self):
        return self.driver.find_elements(*PraisePage.PublicLibrary)

    def Scroll_to(self):
        return self.driver.find_element(*PraisePage.scroll)

    def My_Computer(self):
        return self.driver.find_element(*PraisePage.MyComputer)

    def Browse_btn(self):
        return self.driver.find_element(*PraisePage.browse)

    def Praise_btn(self):
        return self.driver.find_element(*PraisePage.PraiseBtn)

    def screen_shot(self):
        return self.driver.get_screenshot_as_file("screenImage.png")


