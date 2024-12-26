import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None


# syntax to pass command line , if we want to run in different browsers if the below is defined i can simply run this using command prompt
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "Ie":
        driver = webdriver.Ie()

# both test case as the same URL using same fixture
    driver.implicitly_wait(5)
    driver.get("https://pfsmigrationdata.mastmojo.com/sign_in?")
    driver.maximize_window()
    driver.find_element(By.NAME, "user[user_name]").send_keys("niranjanmigration@karnab.com")
    driver.find_element(By.NAME, "user[password]").send_keys("Niranjanmigration@123")
    driver.find_element(By.CLASS_NAME, "signin-btn").click()
    wait = WebDriverWait(driver, 10)  # Explicit wait overrides the Implicit wait
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[@data-value= 'feedback']")))
    driver.get("https://pfsmigrationdata.mastmojo.com/pages/my_corner/feedback#overview")
    request.cls.driver = driver
    yield  # we can't use yield and return statement together , so use above request method
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
