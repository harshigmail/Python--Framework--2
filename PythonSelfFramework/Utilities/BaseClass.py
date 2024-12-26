import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def VerifyPresence(self, text):
        wait = WebDriverWait(self.driver, 10)  # Explicit wait overrides the Implicit wait
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

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
