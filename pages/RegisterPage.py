from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_pwd_field_id = "input-confirm"
    yes_radio_button_xpath = "//label[normalize-space()='Yes']//input[@name='newsletter']"
    agree_field_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"

    def enter_first_name(self, txt_firstname):
        self.type_into_element(txt_firstname, "first_name_field_id", self.first_name_field_id)

    def enter_last_name(self, txt_lastname):
        self.type_into_element(txt_lastname, "last_name_field_id", self.last_name_field_id)

    def enter_email(self, email_txt):
        self.type_into_element(email_txt, "email_field_id", self.email_field_id)

    def enter_telephone(self, telephone_txt):
        self.type_into_element(telephone_txt, "telephone_field_id", self.telephone_field_id)

    def enter_password(self, password_txt):
        self.type_into_element(password_txt, "password_field_id", self.password_field_id)

    def enter_password_confirm(self, password_txt_confirm):
        self.type_into_element(password_txt_confirm, "confirm_pwd_field_id", self.confirm_pwd_field_id)

    def select_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath", self.yes_radio_button_xpath)
        # self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def select_agree_checkbox_field(self):
        self.element_click("_xpath", self.agree_field_xpath)
        # self.driver.find_element(By.XPATH, self.agree_field_xpath).click()

    def click_on_continue_button(self):
        self.element_click("_xpath", self.continue_button_xpath)
        # self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def register_account(self, first_name, last_name, email, telephone, password, confirm, yes_or_no, privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_password_confirm(confirm)
        if yes_or_no == "Yes":
            self.select_yes_radio_button()

        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()

        self.click_on_continue_button()
