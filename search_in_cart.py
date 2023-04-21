import unittest


class GroceryCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity


    def search_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def total_items(self):
        return sum(self.items.values())


