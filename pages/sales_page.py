from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


womens_sales_button_locator = (By.XPATH, "//*[@class='more button'][text()='Shop Women’s Deals']")
mens_sales_icon_locator = (By.XPATH, "//*[@class='more icon'][text()='Shop Men’s Deals']")


class SalesPage(BasePage):
    page = "sale.html"

    womens_sales_button_locator = (By.XPATH, "//*[@class='more button'][text()='Shop Women’s Deals']")
    mens_sales_icon_locator = (By.XPATH, "//*[@class='more icon'][text()='Shop Men’s Deals']")

    def open_women_sales(self):
        self.wait_until_element_is_visible(womens_sales_button_locator)
        womens_sales_button = self.find(womens_sales_button_locator)
        womens_sales_button.click()


    def open_men_sales(self):
        self.wait_until_element_is_visible(mens_sales_icon_locator)
        mens_sales_icon = self.find(mens_sales_icon_locator)
        mens_sales_icon.click()
