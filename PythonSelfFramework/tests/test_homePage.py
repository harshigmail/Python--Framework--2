import time

import pytest

from PythonSelfFramework.PageObjects.HomePage import HomePage
from PythonSelfFramework.TestData.excelHomePageDats import HomePageData1
from PythonSelfFramework.Utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_homePage(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First Name is " + getData["firstname"])
        homePage.names().send_keys(getData["firstname"])
        homePage.emails().send_keys(getData["Email"])
        homePage.passwords().send_keys(getData["Password"])
        homePage.checkboxes().click()
        homePage.radiobuttons().click()
        homePage.submits().click()
        successmessage = homePage.alerts().text
        log.info(successmessage)
        assert "Success!" in successmessage
        time.sleep(5)
        self.driver.refresh()  # used because in the same browser it has taken the next tuple values so we used refresh browser

    # @pytest.fixture(params=[("Rahul", "rahul@gmail.com", "password1"), ("Sri", "shree@gmail.com", "password2")]) # tuple direct values using indexes
    @pytest.fixture(params=HomePageData1.testData1("TestCase2"))  # dictonary it has key
    def getData(self, request):
        return request.param

# if there are more elements with same locator them count your element from top left and add it
# driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Good")

# to clear
# driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
