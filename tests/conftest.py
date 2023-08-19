import pytest
from selenium import webdriver
import time
from utilities import ReadConfigurations


# pip install pytest
# pip install selenium


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    driver = None

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Edge()
    else:
        print("Unknown browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.quit()


@pytest.fixture()
def setup_and_teardown_2(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    driver = None

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Edge()
    else:
        print("Unknown browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = ReadConfigurations.read_configuration("basic info", "url_2")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.quit()
