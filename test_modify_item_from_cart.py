import unittest

from app.modify_in_item_from_cart import modify_item_in_cart


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
