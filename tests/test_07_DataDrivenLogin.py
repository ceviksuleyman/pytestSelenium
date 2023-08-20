import pytest

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email,pwd", ExcelUtils.get_data_from_excel("../ExcelFiles/testdata.XLSX", "LoginData"))
    def test_login_with_valid_credentials(self, email, pwd):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_login_option()

        login_page = LoginPage(self.driver)
        login_page.login_to_application(email, pwd)

        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_account_information_option()
