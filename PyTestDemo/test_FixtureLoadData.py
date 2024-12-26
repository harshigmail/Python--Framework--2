import pytest

from PyTestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_user_profile(self,dataLoad):
        log = self.test_loggingDemo()
        log.info(dataLoad)

