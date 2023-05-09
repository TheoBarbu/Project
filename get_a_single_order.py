import unittest

from app.get_a_single_order import GroceryItem, GroceryOrder
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
        self.item1 = GroceryItem("apples", 0.5, 3)
        self.item2 = GroceryItem("bananas", 0.3, 2)
        self.order = GroceryOrder([self.item1, self.item2])

    def test_total_items(self):
        self.assertEqual(self.order.total_items(), 5)


if __name__ == '__main__':
    unittest.main()
