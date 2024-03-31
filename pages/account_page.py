# pages/account_page.py

from selenium.webdriver.common.by import By


class AccountPageLocators:
    my_account_locator = (
        By.XPATH, "//h1/span[@data-ui-id='page-title-wrapper']")
