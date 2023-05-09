import unittest


class GroceryOrder:
    def __init__(self, items):
        self.items = items

    def total_items(self):
        return sum([item.quantity for item in self.items])


class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


