# pages/home_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.men_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men.html"]',
        )
        self.tops_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men/tops-men.html"]',
        )
        self.bottoms_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men/bottoms-men.html"]',
        )
        self.tops_jackets_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"]',
        )
        self.tops_hoodies_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html"]',
        )
        self.tops_tees_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men/tops-men/tees-men.html"]',
        )
        self.tops_tanks_submenu_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html"]',
        )
        self.cart_locator = (
            By.XPATH,
            '//a[@href="https://magento.softwaretestingboard.com/checkout/cart/"]',
        )
        self.proceed_to_checkout_locator = (
            By.XPATH,
            "//button[@title='Proceed to Checkout']",
        )

    def hover_over_men_menu(self):
        men_submenu = self.driver.find_element(*self.men_submenu_locator)
        ActionChains(self.driver).move_to_element(men_submenu).perform()

    def hover_over_tops_menu(self):
        tops_submenu = self.driver.find_element(*self.tops_submenu_locator)
        ActionChains(self.driver).move_to_element(tops_submenu).perform()

    def click_tops_submenu(self):
        tops_submenu = self.driver.find_element(*self.tops_submenu_locator)
        tops_submenu.click()

    def click_bottoms_submenu(self):
        bottoms_submenu = self.driver.find_element(*self.bottoms_submenu_locator)
        bottoms_submenu.click()

    def click_tops_jackets_submenu(self):
        tops_jackets_submenu = self.driver.find_element(
            *self.tops_jackets_submenu_locator
        )
        tops_jackets_submenu.click()

    def click_tops_hoodies_submenu(self):
        tops_hoodies_submenu = self.driver.find_element(
            *self.tops_hoodies_submenu_locator
        )
        tops_hoodies_submenu.click()

    def click_tops_tees_submenu(self):
        tops_tees_submenu = self.driver.find_element(*self.tops_tees_submenu_locator)
        tops_tees_submenu.click()

    def click_tops_tanks_submenu(self):
        tops_tanks_submenu = self.driver.find_element(*self.tops_tanks_submenu_locator)
        tops_tanks_submenu.click()

    def click_cart(self):
        cart = self.driver.find_element(*self.cart_locator)
        cart.click()

    def proceed_to_checkout(self):
        proceed_to_checkout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.proceed_to_checkout_locator)
        )
        proceed_to_checkout.click()
