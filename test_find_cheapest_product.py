import unittest

from app.find_cheapest_product import find_cheapest_product


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
