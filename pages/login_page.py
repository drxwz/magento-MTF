# pages/login_page.py

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input_locator = (By.ID, 'email')
        self.password_input_locator = (By.ID, "pass")
        self.login_button_locator = (By.ID, "send2")

    def login(self, email, password):
        self.driver.find_element(*self.email_input_locator).send_keys(email)
        self.driver.find_element(
            *self.password_input_locator).send_keys(password)
        self.driver.find_element(*self.login_button_locator).click()
