import pytest

from config.settings import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.account_page import AccountPageLocators


# @pytest.mark.usefixtures("handle_consent")
def test_valid_login(logged_in_browser):
    my_account_element = logged_in_browser.find_element(
        *AccountPageLocators.my_account_locator
    )
    assert (
        my_account_element.is_displayed()
    ), "My account element is not displayed on the new page"


# @pytest.mark.usefixtures("handle_consent")
def test_invalid_login(browser, config):
    browser.get(config["urls"]["login_page"])
    login_page = LoginPage(browser)
    login_page.login(config["wrong_email"], config["wrong_password"])
    assert browser.current_url == config["urls"]["login_page"]
