import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from PythonSelfFramework.PageObjects.CheckoutPage import CheckOutPage
from PythonSelfFramework.PageObjects.ConfirmPage import ConfirmPage
from PythonSelfFramework.PageObjects.HomePage import HomePage
from PythonSelfFramework.Utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        time.sleep(5)
        log.info("getting all the phone details")
        phones = checkOutPage.PhoneItem()
        for phone in phones:
            item = phone.text
            log.info(item)
            if item == "Nokia Edge":
                addtoCart = checkOutPage.ButtonAdd(phone)
                addtoCart.click()

        checkOutPage.CheckoutButton().click()
        confirmPage = checkOutPage.CheckoutButton1()
        time.sleep(5)
        confirmPage.SelectCountries().send_keys("Ind")
        # time.sleep(5)
        self.VerifyPresence("India")  # explicit wait
        countries = confirmPage.ListCountries()
        for country in countries:
            if country.text == 'India':
                country.click()
                break

        confirmPage.Validates().get_attribute("value")
        confirmPage.Purchases().click()
        print(confirmPage.Alerts().text)

        # or

        SuccessText = confirmPage.Successes().text
        log.info("Text received after purchase" +SuccessText)
        assert "Happy! Thank you!" in SuccessText

