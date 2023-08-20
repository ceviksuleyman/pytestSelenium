import time

import pytest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("Blouse")
        self.driver.find_element(By.XPATH, "//button[@name='submit_search']").click()
        self.driver.find_element(By.XPATH,
                                 "//li[@class='clearfix']//a[@class='product-name'][normalize-space()='Blouse']").click()
        assert self.driver.find_element(By.XPATH, "//h1[@itemprop='name']").text == "Blouse"
        time.sleep(2)

    def test_search_for_an_invalid_product(self):
        self.driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("MSI Laptop", Keys.ENTER)
        expected_txt = 'No results were found for your search "MSI Laptop"'
        assert self.driver.find_element(By.XPATH, "//p[@class='alert alert-warning']").text.__eq__(expected_txt)

    def test_search_without_entering_any_product(self):
        self.driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("", Keys.ENTER)
        expected_txt = 'Please enter a search keyword'
        assert self.driver.find_element(By.XPATH, "//p[@class='alert alert-warning']").text.__eq__(expected_txt)
