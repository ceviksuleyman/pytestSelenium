from datetime import datetime

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


def generate_email_with_time_stamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "Cevik" + time_stamp + "@gmail.com"


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_my_account_drop_menu()
        home_page.click_register_option()

        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Smith")
        register_page.enter_last_name("Pytest")
        register_page.enter_email(generate_email_with_time_stamp())
        register_page.enter_telephone("08545456666")
        register_page.enter_password("Qwerty01!")
        register_page.enter_password_confirm("Qwerty01!")
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        # register_page.register_account("Smith", "Pytest",
        #                                generate_email_with_time_stamp(), "08545456666",
        #                                "123456", "123456",
        #                                "No", "select")

        expected_txt = 'Your Account Has Been Created!'
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message() == expected_txt
