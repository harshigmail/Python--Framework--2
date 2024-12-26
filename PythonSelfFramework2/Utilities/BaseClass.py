import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PythonSelfFramework2.PageObjects.FeedbackPage import FeedbackPage
from PythonSelfFramework2.PageObjects.PraisePage import PraisePage
from PythonSelfFramework2.PageObjects.RequestFeedbackPage import RequestFeedbackPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    # share feedback

    def VerifyPresence(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_all_elements_located(
            (By.XPATH, "//ul[contains(@class, 'select2-results__options')]/li")))

    def Attachment_text(self):
        wait = WebDriverWait(self.driver, 10)
        feedbackPage = FeedbackPage(self.driver)
        Attachment = feedbackPage.attachment
        wait.until(expected_conditions.visibility_of_element_located(Attachment))

    def Toaster_text(self):
        wait = WebDriverWait(self.driver, 20)
        feedbackPage = FeedbackPage(self.driver)
        toaster_locator = feedbackPage.Toaster
        wait.until(expected_conditions.presence_of_element_located(toaster_locator))

    # Praise

    def LoadLibrary(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_all_elements_located(
            (By.XPATH, "//div[@id = 'images-list-container']/div")))

    def element_Visible(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//div[@class = 'mb-1 preview-images']/div/img")))

    def MyComputer_attachment(self):
        wait = WebDriverWait(self.driver, 10)
        praisePage = PraisePage(self.driver)
        Attachment = praisePage.AttachmentPraise
        wait.until(expected_conditions.visibility_of_element_located(Attachment))

    def toaster_Praise_Text(self):
        wait = WebDriverWait(self.driver, 20)
        praisePage = PraisePage(self.driver)
        toaster_locator = praisePage.toasterPraise
        wait.until(expected_conditions.presence_of_element_located(toaster_locator))

    def scroll_function(self):
        praisePage = PraisePage(self.driver)
        scrollable_container = praisePage.Scroll_to()
        # Find initially visible elements inside the container
        child_elements = scrollable_container.find_elements(By.XPATH, "./div")
        # Get the count of visible elements
        initial_count = len(child_elements)
        # Scroll and load all elements
        last_count = 0
        while last_count != initial_count:
            last_count = initial_count
        # Scroll to the end of the container
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_container)
        time.sleep(10)  # Wait for new elements to load
        # Count the elements again
        child_elements = scrollable_container.find_elements(By.XPATH, "./div")
        initial_count = len(child_elements)
        print(f"Total number of elements: {initial_count}")
        return initial_count

    # Request Feedback

    def Categories_display(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_all_elements_located(
            (By.XPATH, "//ul[contains(@class, 'select2-results__options')]/li")))

    def Toaster_requestfeedback(self):
        wait = WebDriverWait(self.driver, 20)
        requestfdPage = RequestFeedbackPage(self.driver)
        toaster_locator = requestfdPage.ToasterRequest
        wait.until(expected_conditions.presence_of_element_located(toaster_locator))


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logdata.log')
        formatter = logging.Formatter(
            " %(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
