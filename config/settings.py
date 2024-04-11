# config/settings.py


class Config:
    first_name = "fname"
    last_name = "lname"

    urls = {
        "homepage": "https://magento.softwaretestingboard.com/",
        "login_page": "https://magento.softwaretestingboard.com/customer/account/login/",
        "account_page": "https://magento.softwaretestingboard.com/customer/account/",
        "checkout_page": "https://magento.softwaretestingboard.com/checkout",
        "checkout_cart_page": "https://magento.softwaretestingboard.com/checkout/cart/",
        "checkout_page": "https://magento.softwaretestingboard.com/checkout/#shipping",
        "payment_page": "https://magento.softwaretestingboard.com/checkout/#payment",
    }

    email = "fnamelname@email.com"
    password = "FNAMElname!"
    wrong_email = "invalidEmail@email.com"
    wrong_password = "invalidPassword"
