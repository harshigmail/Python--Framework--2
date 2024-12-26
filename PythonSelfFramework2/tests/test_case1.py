import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from PythonSelfFramework2.PageObjects.FeedbackPage import FeedbackPage
from PythonSelfFramework2.Utilities.BaseClass import BaseClass

file_path = "C:\\Users\\harshitha.n\\Downloads\\30-Day Employee Performance Review Template.pdf"
class TestCase1(BaseClass):

    def test_case1(self):
        log = self.getLogger()
        feedbackPage = FeedbackPage(self.driver)
        feedbackPage.ModuleClick().click()
        feedbackPage.AboutName().send_keys("San")
        time.sleep(5)
        user_names = feedbackPage.User_Names()
        log.info("Store all the usernames")
        for user in user_names:
            if "Sanjay Kumar" in user.text:
                user.click()
                break
        time.sleep(2)
        feedbackPage.Text_field().send_keys("Add Goals for this year 2024")
        Radiobuttons = feedbackPage.Radio_Buttons()
        print(len(Radiobuttons))
        for radiobutton in Radiobuttons:
            print(radiobutton.text)
            if radiobutton.text == "Development Opportunity":
                radiobutton.click()
                log.info("Radio button is selected successfully")
        # print(f"Is selected: {radiobutton.is_selected()}")

        feedbackPage.Category_Click().click()
        self.VerifyPresence()
        Categories = feedbackPage.Categories_List()
        print(len(Categories))
        for category in Categories:
            if category.get_attribute("title") == "Uses sound judgment to make good decisions based on information gathered and analyzed. Considers all pertinent facts and alternatives before deciding on the most appropriate action. Commits to decision.":
                category.click()
                break
        time.sleep(1)

        attach_button = feedbackPage.Attach_Button()
        attach_button.send_keys(file_path)
        Attachment = feedbackPage.attachment
        self.Attachment_text()
        print(self.driver.find_element(*Attachment).text)

        feedbackPage.Submit_Click().click()
        toaster_locator = feedbackPage.Toaster
        self.Toaster_text()
        print(self.driver.find_element(*toaster_locator).text)

