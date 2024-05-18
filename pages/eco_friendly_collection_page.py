from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


first_item_locator = (By.XPATH, "//*[@data-product-id='2017']")
add_to_compare_button_locator = (By.XPATH, "//*[@title='Add to Compare']")
first_compare_item_locator = (By.XPATH, "//a[text()='Ana Running Short']")
add_to_cart_button_locator = (By.XPATH, "//form[@data-product-sku='WSH10']//button[@title='Add to Cart']")
clear_compare_items_button_locator = (By.XPATH, "//*[@id='compare-clear-all']")
popup_accept_button_locator = (By.XPATH, "//button[contains(@class, 'action-accept')]")


class EcoFriendlyCollectionPage(BasePage):
    page = "collections/eco-friendly.html"

    def add_to_compare(self):
        actions = ActionChains(self.driver)
        first_item = self.find(first_item_locator)
        add_to_compare_button = self.find(add_to_compare_button_locator)
        actions.move_to_element(first_item).move_to_element(add_to_compare_button).click(add_to_compare_button).perform()


    def check_compared_item_added(self):
        self.wait.until(EC.presence_of_element_located(first_compare_item_locator))
        first_compare_item = self.find(first_compare_item_locator)
        first_compare_item.is_displayed()


    def add_item_to_cart(self):
        actions = ActionChains(self.driver)
        first_item = self.find(first_item_locator)
        add_to_cart_button = self.find(add_to_cart_button_locator)
        actions.move_to_element(first_item).move_to_element(add_to_cart_button).click(add_to_cart_button).perform()


    def clear_compare_items(self):
        clear_compare_items_button = self.find(clear_compare_items_button_locator)
        clear_compare_items_button.click()
        self.wait.until(EC.visibility_of_element_located(popup_accept_button_locator))
        popup_accept_button = self.find(popup_accept_button_locator)
        popup_accept_button.click()


    def check_compare_item_is_not_visible(self):
        self.wait.until(EC.invisibility_of_element_located(first_compare_item_locator))
