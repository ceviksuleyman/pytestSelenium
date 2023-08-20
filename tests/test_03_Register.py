import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()


def test_register_with_mandatory_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Cevik")
    driver.find_element(By.ID, "input-lastname").send_keys("Pytest")
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.ID, "input-telephone").send_keys("08555445544")
    driver.find_element(By.ID, "input-password").send_keys("Pytest01.")
    driver.find_element(By.ID, "input-confirm").send_keys("Pytest01.")
    driver.find_element(By.XPATH, "//input[@name='agree']").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    expected_txt = 'Your Account Has Been Created!'
    assert driver.find_element(By.CSS_SELECTOR, "#content>h1").text == expected_txt
    time.sleep(2)
    driver.quit()


def test_register_with_all_fields(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Cevik")
    driver.find_element(By.ID, "input-lastname").send_keys("Pytest")
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.ID, "input-telephone").send_keys("08555445544")
    driver.find_element(By.ID, "input-password").send_keys("Pytest01.")
    driver.find_element(By.ID, "input-confirm").send_keys("Pytest01.")
    driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()
    driver.find_element(By.XPATH, "//input[@name='agree']").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    expected_txt = 'Your Account Has Been Created!'
    assert driver.find_element(By.CSS_SELECTOR, "#content>h1").text == expected_txt
    time.sleep(2)
    driver.quit()


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "cevik" + time_stamp + "@gmail.com"
