import unittest

from app.find_expensive_product import find_expensive_product


class TestCart(unittest.TestCase):

    def test_find_expensive_product(self):
        cart = [
            {'name': 'product1', 'price': 10},
            {'name': 'product2', 'price': 20},
            {'name': 'product3', 'price': 30}
        ]

        result = find_expensive_product(cart)
        expected_result = {'name': 'product3', 'price': 30}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()





