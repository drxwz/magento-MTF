# pages/jackets.py

import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Jackets:
    def __init__(self, driver):
        self.driver = driver
        self.lando_jacket_locator = (
            By.XPATH,
            '(//a[@href="https://magento.softwaretestingboard.com/lando-gym-jacket.html"])[2]',
        )
        self.add_to_cart_locator = (
            By.XPATH,
            "//button[contains(@id, 'product-addtocart-button')]",
        )

    def click_lando_gym_jacket(self):
        lando_gym_jacket = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.lando_jacket_locator))
        lando_gym_jacket.click()

    def select_product(self, product_name):
        if product_name == "lando_gym_jacket":
            self.click_lando_gym_jacket()

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_locator))
        add_to_cart_button.click()


class JacketPageDetails:
    def __init__(self, driver):
        self.driver = driver
        self.size_locator = {
            "XS": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option text') and @option-tooltip-value='XS']",
            ),
            "S": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option text') and @option-tooltip-value='S']",
            ),
            "M": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option text') and @option-tooltip-value='M']",
            ),
            "L": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option text') and @option-tooltip-value='L']",
            ),
            "XL": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option text') and @option-tooltip-value='XL']",
            ),
        }

        self.color_locator = {
            "Blue": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option color') and @option-label='Blue']",
            ),
            "Gray": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option color') and @option-label='Gray']",
            ),
            "Green": (
                By.XPATH,
                "//div[contains(@class, 'swatch-option color') and @option-label='Green']",
            ),
        }

    def select_size(self):
        size = random.choice(list(self.size_locator.keys()))
        size_locator = self.size_locator.get(size)
        if size_locator:
            size_option = self.driver.find_element(*size_locator)
            size_option.click()
        else:
            print(f"Size '{size}' locator not found.")

    def select_color(self):
        color = random.choice(list(self.color_locator.keys()))
        color_locator = self.color_locator.get(color)
        if color_locator:
            color_option = self.driver.find_element(*color_locator)
            color_option.click()
        else:
            print(f"Color '{color}' locator not found.")
