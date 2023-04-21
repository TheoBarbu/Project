import unittest

def find_cheapest_product(cart):
    cheapest_product = min(cart, key=lambda x: x['price'])
    return cheapest_product

