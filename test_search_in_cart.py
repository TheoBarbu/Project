import unittest

from app.search_in_cart import GroceryCart


class TestGroceryCart(unittest.TestCase):
    def setUp(self):
        self.cart = GroceryCart()
        self.item1 = Item("apples", 0.5)
        self.item2 = Item("bananas", 0.3)

    def test_add_item(self):
        self.cart.add_item(self.item1, 3)
        self.assertEqual(self.cart.total_items(), 3)

        self.cart.add_item(self.item2, 2)
        self.assertEqual(self.cart.total_items(), 5)


    def test_search_item(self):
        self.cart.add_item(self.item1, 3)
        self.cart.add_item(self.item2, 2)

        result = self.cart.search_item("apples")
        self.assertEqual(result.name, "apples")

        result = self.cart.search_item("oranges")
        self.assertIsNone(result)

    def test_total_cost(self):
        self.cart.add_item(self.item1, 3)
        self.cart.add_item(self.item2, 2)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    unittest.main()
