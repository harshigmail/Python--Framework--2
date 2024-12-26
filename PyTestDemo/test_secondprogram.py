import pytest


def test_secondProgram():
    msg = "Hello"
    assert msg == "Hi", "Test case failed strings doesn't matched"


@pytest.mark.smoke   # grouping test case /method for regression suite
def test_thirdProgramCard():
    a = 4
    b = 2
    assert a + 2 == 6, "Addition doesn't match"
