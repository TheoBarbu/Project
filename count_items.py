import unittest


class GroceryCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity


    def count_items(self):
        return len(self.items)

    def total_cost(self):
        return sum([item.price * quantity for item, quantity in self.items.items()])


