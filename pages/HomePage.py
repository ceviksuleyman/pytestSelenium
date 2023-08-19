from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box = "//input[@placeholder='Search']"
    search_button = "//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath = "//span[normalize-space()='My Account']"
    login_option_link = "Login"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box).click()
        self.driver.find_element(By.XPATH, self.search_box).clear()
        self.driver.find_element(By.XPATH, self.search_box).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button).click()

    def click_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def click_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link).click()
