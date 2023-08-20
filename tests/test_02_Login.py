import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By


def generate_email_with_time_stamp():
    # time_stamp = datetime.now().strftime("%Y-%m-%dT%H")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "pytest" + time_stamp + "@gmail.com"


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//a[@class='login']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("pytest@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd").send_keys("Pytest01!")
        self.driver.find_element(By.CSS_SELECTOR, "button#SubmitLogin").click()
        assert self.driver.find_element(By.XPATH, "//span[normalize-space()='Pytest Demo']").text.__eq__("Pytest Demo")
        time.sleep(2)

    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.find_element(By.XPATH, "//a[@class='login']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(generate_email_with_time_stamp())
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd").send_keys("Pytest01!")
        self.driver.find_element(By.CSS_SELECTOR, "button#SubmitLogin").click()
        expected_text = "Authentication failed."
        assert self.driver.find_element(By.XPATH, "//li[normalize-space()='Authentication failed.']").text.__eq__(
            expected_text)
        time.sleep(2)

    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.find_element(By.XPATH, "//a[@class='login']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("pytest@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd").send_keys("Pytest0")
        self.driver.find_element(By.CSS_SELECTOR, "button#SubmitLogin").click()
        expected_text = "Authentication failed."
        assert self.driver.find_element(By.XPATH, "//li[normalize-space()='Authentication failed.']").text.__eq__(
            expected_text)
        time.sleep(2)

    def test_test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//a[@class='login']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "button#SubmitLogin").click()
        expected_text = "An email address required."
        assert (self.driver.find_element(By.XPATH, "//li[normalize-space()='An email address required.']")
                .text.__eq__(expected_text))
        time.sleep(2)
