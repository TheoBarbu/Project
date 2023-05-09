import unittest

from app.modify_in_item_from_cart import modify_item_in_cart
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

    def test_modify_item_in_cart(self):
        cart = [
            {'name': 'product1', 'price': 10},
            {'name': 'product2', 'price': 20},
            {'name': 'product3', 'price': 30}
        ]
        result = modify_item_in_cart(cart, 'product2', 25)
        expected_result = [
            {'name': 'product1', 'price': 10},
            {'name': 'product2', 'price': 25},
            {'name': 'product3', 'price': 30}
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
