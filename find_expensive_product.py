import unittest

def find_expensive_product(cart):
    most_expensive_product = max(cart, key=lambda x: x['price'])
    return most_expensive_product


