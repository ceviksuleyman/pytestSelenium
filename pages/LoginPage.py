from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"

    def enter_email_address(self, email_address_txt):
        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address_txt)

    def enter_password(self, password_txt):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_txt)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()