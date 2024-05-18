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
        self.wait.until(EC.visibility_of_element_located(first_name_field_locator))
        first_name_field = self.find(first_name_field_locator)
        first_name_field.send_keys(first_name)


    def add_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located(last_name_field_locator))
        last_name_field = self.find(last_name_field_locator)
        last_name_field.send_keys(last_name)


    def add_email(self, email):
        self.wait.until(EC.visibility_of_element_located(email_field_locator))
        email_field = self.find(email_field_locator)
        email_field.send_keys(email)


    def add_password(self, password):
        self.wait.until(EC.visibility_of_element_located(password_field_locator))
        self.wait.until(EC.visibility_of_element_located(password_confirm_field_locator))
        password_field = self.find(password_field_locator)
        password_field.send_keys(password)
        confirm_password_field = self.find(password_confirm_field_locator)
        confirm_password_field.send_keys(password)


    def click_create_account_button(self):
        self.wait.until(EC.visibility_of_element_located(create_account_button_locator))
        create_account_button = self.find(create_account_button_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", create_account_button)
        create_account_button.click()
