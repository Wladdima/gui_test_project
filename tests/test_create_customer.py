import pytest
import random


first_name = "Max"
last_name = "Mustermann"
random_number = random.randint(1,1000)
email = f"max_mustermann{random_number}@email.com"
password = "$Admin1234"
my_account_page_url = "customer/account/"
create_account_page_url = "customer/account/create/"


@pytest.mark.positive
@pytest.mark.smoke
def test_create_new_customer(create_customer_page):
    create_customer_page.open_page()
    create_customer_page.add_first_name(first_name)
    create_customer_page.add_last_name(last_name)
    create_customer_page.add_email(email)
    create_customer_page.add_password(password)
    create_customer_page.click_create_account_button()
    create_customer_page.check_page(my_account_page_url)


@pytest.mark.negative
@pytest.mark.extended
def test_create_user_with_nonunique_email(create_customer_page):
    create_customer_page.open_page()
    create_customer_page.add_first_name(first_name)
    create_customer_page.add_last_name(last_name)
    create_customer_page.add_email("max_mustermann@email.com")
    create_customer_page.add_password(password)
    create_customer_page.click_create_account_button()
    create_customer_page.check_page(create_account_page_url)


@pytest.mark.negative
@pytest.mark.extended
def test_create_user_without_name(create_customer_page):
    create_customer_page.open_page()
    create_customer_page.add_first_name()
    create_customer_page.add_last_name(last_name)
    create_customer_page.add_email(email)
    create_customer_page.add_password(password)
    create_customer_page.click_create_account_button()
    create_customer_page.check_page(create_account_page_url)
    create_customer_page.check_field_required_error_message("firstname")
