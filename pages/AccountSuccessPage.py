from selenium.webdriver.common.by import By


class AccountSuccessPage:

    def __init__(self, driver):
        self.driver = driver

    account_creation_message_xpath = "#content>h1"

    def retrieve_account_creation_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.account_creation_message_xpath).text
