import time


from PythonSelfFramework2.PageObjects.RequestFeedbackPage import RequestFeedbackPage
from PythonSelfFramework2.Utilities.BaseClass import BaseClass

file_path = "C:\\Users\\harshitha.n\\Downloads\\30-Day Employee Performance Review Template.pdf"


class TestCase3(BaseClass):

    def test_case3(self):
        log = self.getLogger()
        requestfdPage = RequestFeedbackPage(self.driver)
        requestfdPage.ModuleClick().click()
        Radiobuttons = requestfdPage.Radio_Buttons()
        print(len(Radiobuttons))
        for radiobutton in Radiobuttons:
            print(radiobutton.text)
            if radiobutton.text == "Someone":
                radiobutton.click()
        time.sleep(1)
        requestfdPage.Some_One().click()
        requestfdPage.SomeOne_Data().send_keys("San")
        time.sleep(8)
        log.info("storing all the usernames1")
        user_names = requestfdPage.User_Names()
        for user in user_names:
            if "Sandyashree Kumar" in user.text:
                user.click()
                break
        time.sleep(3)
        requestfdPage.From_recepient().send_keys("San")
        time.sleep(8)
        log.info("storing all the usernames2")
        user_names = requestfdPage.From_User_Names()
        for user in user_names:
            if "Sanjay Kumar" in user.text:
                user.click()
                break
        time.sleep(3)
        requestfdPage.Text_Field().send_keys("Request feedback- year 2023")
        requestfdPage.Category_click().click()
        self.Categories_display()
        log.info("storing all the Categories")
        Categories = requestfdPage.Categories_List()
        print(len(Categories))
        for category in Categories:
            if category.get_attribute("title") == "Uses sound judgment to make good decisions based on information gathered and analyzed. Considers all pertinent facts and alternatives before deciding on the most appropriate action. Commits to decision.":
                category.click()
                break
        time.sleep(1)
        requestfdPage.Submit_btn().click()
        toaster_locator = requestfdPage.ToasterRequest
        self.Toaster_requestfeedback()
        print(self.driver.find_element(*toaster_locator).text)
        log.info("Posted Successfully")

