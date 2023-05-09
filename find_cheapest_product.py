import unittest

from app.find_cheapest_product import find_cheapest_product

import softest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestShopifyGroceriesPage(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://www.freshful.ro/")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

class TestCart(unittest.TestCase):

    def test_find_cheapest_product(self):
        cart = [
            {'name': 'product1', 'price': 10},
            {'name': 'product2', 'price': 20},
            {'name': 'product3', 'price': 5}
        ]
        result = find_cheapest_product(cart)
        expected_result = {'name': 'product3', 'price': 5}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
