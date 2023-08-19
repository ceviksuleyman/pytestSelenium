from datetime import time

import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.AccountPage import AccountPage


@pytest.mark.usefixtures("setup_and_teardown_2")
class TestLogin:

    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_login_option()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address("automation01@gmail.com")
        login_page.enter_password("123456")
        login_page.click_login_button()

        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_account_information_option()
