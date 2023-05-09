import unittest

from app.create_order import GroceryOrder
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


class TestGroceryOrder(unittest.TestCase):
    def setUp(self):
        self.order = GroceryOrder()
        self.item1 = Item("apples", 0.5)
        self.item2 = Item("bananas", 0.3)

    def test_add_item(self):
        self.order.add_item(self.item1, 3)
        self.assertEqual(self.order.total_items(), 3)

        self.order.add_item(self.item2, 2)
        self.assertEqual(self.order.total_items(), 5)

    def test_remove_item(self):
        self.order.add_item(self.item1, 3)
        self.order.add_item(self.item2, 2)

        self.order.remove_item(self.item1, 2)
        self.assertEqual(self.order.total_items(), 3)

        self.order.remove_item(self.item1, 1)
        self.assertEqual(self.order.total_items(), 2)

        with self.assertRaises(ValueError):
            self.order.remove_item(self.item2, 3)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    unittest.main()
