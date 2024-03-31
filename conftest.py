import pytest
from config.settings import Config
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.account_page import AccountPageLocators
from config.settings import Config


@pytest.fixture(scope="session")
def config():
    return {
        "first_name": Config.first_name,
        "last_name": Config.last_name,
        "urls": Config.urls,
        "email": Config.email,
        "password": Config.password,
        "wrong_email": Config.wrong_email,
        "wrong_password": Config.wrong_password,
    }


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup before each test
    print("\n--------------------Setup before each test--------------------\n")

    yield

    # Teardown after each test
    print("\n--------------------Teardown after each test--------------------\n")


@pytest.fixture
def logged_in_browser(request, browser, config):
    # Setup: Perform login
    if "test_valid_login" or "test_invalid_login" not in request.node.name:
        browser.get(config["urls"]["login_page"])
        login_page = LoginPage(browser)
        login_page.login(config["email"], config["password"])
        assert browser.current_url == config["urls"]["account_page"]
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                AccountPageLocators.my_account_locator)
        )
        my_account_element = browser.find_element(
            *AccountPageLocators.my_account_locator
        )
        assert (my_account_element.is_displayed(
        )),             "My account element is not displayed on the new page"

    return browser
