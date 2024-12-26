import pytest


@pytest.mark.usefixtures("crossBrowser")
def test_user_profile(crossBrowser):
    print(crossBrowser)
