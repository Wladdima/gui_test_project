import pytest
from time import sleep


first_item_page = "ana-running-short.html"


@pytest.mark.positive
@pytest.mark.smoke
def test_add_item_to_compare(eco_friendly_collection_page):
    eco_friendly_collection_page.open_page()
    eco_friendly_collection_page.add_to_compare()
    eco_friendly_collection_page.check_compared_item_added()


@pytest.mark.positive
@pytest.mark.smoke
def test_add_item_to_cart(eco_friendly_collection_page):
    eco_friendly_collection_page.open_page()
    eco_friendly_collection_page.add_item_to_cart()
    eco_friendly_collection_page.check_page(first_item_page)


@pytest.mark.positive
@pytest.mark.extended
def test_clear_comare_items(eco_friendly_collection_page):
    eco_friendly_collection_page.open_page()
    eco_friendly_collection_page.add_to_compare()
    eco_friendly_collection_page.check_compared_item_added()
    eco_friendly_collection_page.clear_compare_items()
    eco_friendly_collection_page.check_compare_item_is_not_visible()
