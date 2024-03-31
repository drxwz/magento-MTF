import pytest
import time

from config.product_urls import ProductURLs
from pages.homepage import HomePage
from pages.jackets import Jackets, JacketPageDetails
from pages.checkout_page import Checkout
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("product_name", ["lando_gym_jacket"])
def test_successful_order_placement(browser, config, logged_in_browser, product_name):
    # Find an item
    home_page = HomePage(browser)
    home_page.hover_over_men_menu()
    home_page.hover_over_tops_menu()
    home_page.click_tops_jackets_submenu()
    product_urls = ProductURLs()
    assert browser.current_url == product_urls.get_url("men_tops_jackets_page")

    # Select the item
    jackets = Jackets(browser)
    jackets.select_product(product_name)
    assert browser.current_url == product_urls.get_url(product_name)
    time.sleep(2)

    # Choose size and color
    jacket_details = JacketPageDetails(browser)
    jacket_details.select_color()
    jacket_details.select_size()

    # Add item to cart
    jackets.add_to_cart()
    time.sleep(5)

    # Check cart
    home_page.click_cart()
    time.sleep(1)
    home_page.proceed_to_checkout()
    time.sleep(5)
    assert browser.current_url == config["urls"]["checkout_page"]

    # Fill the forms
    checkout_page = Checkout(browser)
    checkout_page.fill_checkout_fields()
    time.sleep(2)
