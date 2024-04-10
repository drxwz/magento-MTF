from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input_locator = (By.XPATH, "//input[@id='email']")
        self.password_input_locator = (By.XPATH, "//input[@id='pass']")
        self.login_button_locator = (By.XPATH, "//button[@id='send2']")
        self.consent_element_locator = (By.XPATH, "//p[@class='fc-button-label' and contains(text(), 'Consent')]")

    def handle_consent_button(self):
        try:
            consent_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.consent_element_locator)
            )
            consent_element.click()
        except:
            pass

    def check_consent_element_present(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.consent_element_locator)
            )
            return True
        except:
            return False

    def login(self, email, password):
        # Handle consent button if present
        self.handle_consent_button()

        # Continue with login logic
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input_locator)
        )
        email_input.send_keys(email)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input_locator)
        )
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        )
        login_button.click()
