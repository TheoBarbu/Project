import unittest

from app.replace_an_item_from_cart import replace_item_in_cart
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

    def test_replace_item_in_cart(self):
        cart = [
            {'name': 'product1', 'price': 10},
            {'name': 'product2', 'price': 20},
            {'name': 'product3', 'price': 30}
        ]

        new_item = {'name': 'product4', 'price': 40}
        result = replace_item_in_cart(cart, 'product2', new_item)
        expected_result = [
            {'name': 'product1', 'price': 10},
            {'name': 'product4', 'price': 40},
            {'name': 'product3', 'price': 30}
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
