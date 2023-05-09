class GroceryOrder:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if item not in self.items:
            raise ValueError("Item not in order")
        elif quantity > self.items[item]:
            raise ValueError("Quantity greater than order")
        else:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]

    def total_items(self):
        return sum(self.items.values())


