# config/product_urls.py


class ProductURLs:
    def __init__(self):
        self.urls = {
            "argus_all_weather_tank": "https://magento.softwaretestingboard.com/argus-all-weather-tank.html",
            "hero_hoodie": "https://magento.softwaretestingboard.com/hero-hoodie.html",
            "typhon_performance_fleece_lined_jacket": "https://magento.softwaretestingboard.com/typhon-performance-fleece-lined-jacket.html",
            "lando_gym_jacket": "https://magento.softwaretestingboard.com/lando-gym-jacket.html",
            "men_page": "https://magento.softwaretestingboard.com/men.html",
            "men_tops_page": "https://magento.softwaretestingboard.com/men/tops-men.html",
            "men_tops_jackets_page": "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html",
            "men_tops_hoodies_page": "https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html",
            "men_tops_tees_page": "https://magento.softwaretestingboard.com/men/tops-men/tees-men.html",
            "men_tops_tanks_page": "https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html",
        }

    def get_url(self, product_name):
        return self.urls.get(product_name)
