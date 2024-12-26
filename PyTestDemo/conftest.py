import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute this first")
    yield
    print("I will executed last")


@pytest.fixture
def dataLoad():
    print("User profile data")
    return ["Rahul", "shetty", "rahulshetty.com"]



@pytest.fixture(params=[("chrome", "Rahul", "shetty"),"Firefox", "IE"])
def crossBrowser(request):
    return request.param

