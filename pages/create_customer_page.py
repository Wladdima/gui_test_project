from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


first_name_field_locator = (By.ID, "firstname")
last_name_field_locator = (By.ID, "lastname")
email_field_locator = (By.ID, "email_address")
password_field_locator = (By.ID, "password")
password_confirm_field_locator = (By.ID, "password-confirmation")
create_account_button_locator = (By.XPATH, "//button[contains(@class, 'submit')]")


class CreateCustomerPage(BasePage):
    page = "customer/account/create/"


    def add_first_name(self, first_name=""):
        self.wait_until_element_is_visible(first_name_field_locator)
        first_name_field = self.find(first_name_field_locator)
        first_name_field.send_keys(first_name)


    def add_last_name(self, last_name):
        self.wait_until_element_is_visible(last_name_field_locator)
        last_name_field = self.find(last_name_field_locator)
        last_name_field.send_keys(last_name)


    def add_email(self, email):
        self.wait_until_element_is_visible(email_field_locator)
        email_field = self.find(email_field_locator)
        email_field.send_keys(email)


    def add_password(self, password):
        self.wait_until_element_is_visible(password_field_locator)
        self.wait_until_element_is_visible(password_confirm_field_locator)
        password_field = self.find(password_field_locator)
        password_field.send_keys(password)
        confirm_password_field = self.find(password_confirm_field_locator)
        confirm_password_field.send_keys(password)


    def click_create_account_button(self):
        self.wait_until_element_is_visible(create_account_button_locator)
        create_account_button = self.find(create_account_button_locator)
        self.scroll_to_element(create_account_button)
        create_account_button.click()
