from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import us
import random


class Checkout:

    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker()
        self.checkout_fields = {
            "company_field_locator": (By.XPATH, "//input[@name='company']"),
            "street_address_field_locator": (By.XPATH, "//input[@name='street[0]']"),
            "city_field_locator": (By.XPATH, "//input[@name='city']"),
            "zip_field_locator": (By.XPATH, "//input[@name='postcode']"),
            "phone_number_field_locator": (By.XPATH, "//input[@class='input-text' and @type='text' and @name='telephone']"),
            "country_dropdown_locator": (By.XPATH, "//select[@name='country_id']"),
            "state_dropdown_locator": (By.XPATH, "//select[@name='region_id']"),
            "tablerate_shipping_method": (By.XPATH, "//input[@type='radio' and contains(@class, 'radio') and @value='tablerate_bestway']"),
            "fixed_shipping_method": (By.XPATH, "//input[@type='radio' and contains(@class, 'radio') and @value='flatrate_flatrate']"),
            "next_button": (By.XPATH, "//button[@data-role='opc-continue' and contains(@class, 'button') and contains(@class, 'continue') and contains(@class, 'primary')]"),
        }

    def fill_checkout_fields(self):
        for field_name, locator in self.checkout_fields.items():
            if field_name == "country_dropdown_locator":
                self.select_random_country_and_state(
                    locator, self.checkout_fields["state_dropdown_locator"]
                )
            elif field_name == "state_dropdown_locator":
                continue
            else:
                field_value = self.generate_field_value(field_name)
                if field_value:
                    self.driver.find_element(*locator).send_keys(field_value)

    def generate_field_value(self, field_name):
        if field_name == "company_field_locator":
            return self.fake.company()
        elif field_name == "street_address_field_locator":
            return self.fake.street_address()
        elif field_name == "city_field_locator":
            return self.fake.city()
        elif field_name == "zip_field_locator":
            return self.fake.zipcode()
        elif field_name == "phone_number_field_locator":
            return self.fake.phone_number()
        else:
            return None

    def select_random_country_and_state(self, country_locator, state_locator):
        country_dropdown = Select(self.driver.find_element(*country_locator))
        state_dropdown = Select(self.driver.find_element(*state_locator))
        country_dropdown.select_by_visible_text("United States")
        random_state = random.choice(us.states.STATES)
        state_dropdown.select_by_visible_text(random_state.name)

    def select_shipment(self):
        random_index = random.randint(0, 1)
        selected_shipping_method_key = "tablerate_shipping_method" if random_index == 0 else "fixed_shipping_method"
        selected_radio_button_xpath = self.checkout_fields[selected_shipping_method_key]
        selected_radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(selected_radio_button_xpath)
        )
        selected_radio_button.click()

    def click_next_button(self):
        next_button_locator = self.checkout_fields.get("next_button")
        if next_button_locator:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(next_button_locator)
            )
            next_button.click()
        else:
            print("Next button locator not found in checkout fields.")
