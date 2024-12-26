import pytest


def test_thirdProgramCard():
    a = 4
    b = 2
    assert b + 2 == 4, "Addition doesn't match"


# @pytest.mark.skip # will skip this test
@pytest.mark.xfail # will run but won't show the output
def test_HelloProgram():
    msg = "Hello1"
    assert msg == "Hi1", "Test case failed strings doesn't matched"
