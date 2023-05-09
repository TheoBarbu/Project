import unittest

from app.get_all_items import GroceryCart
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


class TestGroceryCart(unittest.TestCase):
    def setUp(self):
        self.cart = GroceryCart()
        self.item1 = Item("apples", 0.5)
        self.item2 = Item("bananas", 0.3)

    def test_add_item(self):
        self.cart.add_item(self.item1, 3)
        self.assertEqual(self.cart.count_items(), 1)

        self.cart.add_item(self.item2, 2)
        self.assertEqual(self.cart.count_items(), 2)

    def test_total_cost(self):
        self.cart.add_item(self.item1, 3)
        self.cart.add_item(self.item2, 2)

    def test_get_all_items(self):
        self.cart.add_item(self.item1, 3)
        self.cart.add_item(self.item2, 2)
        self.assertCountEqual(self.cart.get_all_items(), [self.item1, self.item2])


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    unittest.main()
