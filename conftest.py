from selenium import webdriver
import pytest
from pages.create_customer_page import CreateCustomerPage
from pages.eco_friendly_collection_page import EcoFriendlyCollectionPage
from pages.sales_page import SalesPage
from time import sleep


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument('--remote-debugging-pipe')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    sleep(3)


@pytest.fixture
def create_customer_page(driver):
    return CreateCustomerPage(driver)


@pytest.fixture
def eco_friendly_collection_page(driver):
    return EcoFriendlyCollectionPage(driver)


@pytest.fixture
def sales_page(driver):
    return SalesPage(driver)
