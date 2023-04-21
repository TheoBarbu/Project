import unittest

from app.replace_an_item_from_cart import replace_item_in_cart


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
