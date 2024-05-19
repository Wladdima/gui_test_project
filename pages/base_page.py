from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page = None


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    def open_page(self):
        if self.page:
            self.driver.get(f"{self.base_url}/{self.page}")
        else:
            raise NotImplementedError('Page can not be opened for this page class')


    def find(self, locator):
        return self.driver.find_element(*locator)


    def check_page(self, check_page):
        self.wait.until(EC.url_matches(f"{self.base_url}/{check_page}"))
        assert self.driver.current_url == f"{self.base_url}/{check_page}"


    def check_field_required_error_message(self, field):
        field_required_error_message_locator = (By.XPATH, f"//*[@id='{field}-error']")
        field_required_error_message = self.find(field_required_error_message_locator)
        assert field_required_error_message.is_displayed()


    def check_element_text(self, locator, text):
        element_text = self.driver.find_element(*locator).text
        assert element_text == text


    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)


    def wait_until_element_is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))


    def wait_until_element_is_not_visible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
