import pytest


@pytest.fixture()
def test_setup():
    print("I will execute this first")
    yield
    print("I will executed last")


def test_fixtureDemo(setup):
    print("execute steps in fixturedemo method")


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("execute steps in fixturedemo1 method")

    def test_fixtureDemo2(self):
        print("execute steps in fixturedemo2 method")

    def test_fixtureDemo3(self):
        print("execute steps in fixturedemo3 method")
