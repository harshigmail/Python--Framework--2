import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from PythonSelfFramework2.PageObjects.PraisePage import PraisePage
from PythonSelfFramework2.Utilities.BaseClass import BaseClass

file_path = "C:\\Users\\harshitha.n\\Downloads\\30-Day Employee Performance Review Template.pdf"


class TestCase2(BaseClass):

    def test_case2(self):
        log = self.getLogger()
        praisePage = PraisePage(self.driver)
        praisePage.ModuleClick().click()
        praisePage.AboutName().send_keys("San")
        time.sleep(3)
        log.info("storing all the usernames")
        user_names = praisePage.User_Names()
        for user in user_names:
            if "Sanjay Kumar" in user.text:
                user.click()
                break
        time.sleep(2)
        praisePage.Text_field().send_keys(" Praise San for last year 2023")
        Tags = praisePage.Tags
        for Tag in Tags:
            Tag1 = praisePage.Tag_assign()
            Tag1.send_keys(Tag)
            Tag1.send_keys(Keys.ENTER)
        time.sleep(5)

        Public_library = praisePage.Public_Library()
        print(len(Public_library))
        for item in Public_library:
            if "Praise" in item.text:
                item.click()
        self.LoadLibrary()
        self.scroll_function()
        scrollable_container = praisePage.Scroll_to()
        child_elements = scrollable_container.find_elements(By.XPATH, "./div")
        for element in child_elements:
            image = element.find_element(By.TAG_NAME, "img")
            if image.get_attribute("src") == "https://cdn.mastmojo.com/engagedly_image_library/Great.png":
                self.driver.execute_script("arguments[0].scrollIntoView();", image)
                image.click()
                print("Image clicked successfully")
                break
        self.element_Visible()
        print("Preview element is visible")
        log.info("Preview element is visible")
        # screenshot of image
        praisePage.screen_shot()
        praisePage.My_Computer().click()
        time.sleep(3)
        browse_button = praisePage.Browse_btn()
        browse_button.send_keys(file_path)
        Attachment = praisePage.AttachmentPraise
        self.MyComputer_attachment()
        print(self.driver.find_element(*Attachment).text)

        praisePage.Praise_btn().click()
        toaster_locator = praisePage.toasterPraise
        self.toaster_Praise_Text()
        print(self.driver.find_element(*toaster_locator).text)
        log.info("Posted Successfully")

