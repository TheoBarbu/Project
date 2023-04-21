import unittest

def modify_item_in_cart(cart, item_name, new_price):
    index = -1
    for i, item in enumerate(cart):
        if item['name'] == item_name:
            index = i
            break
    if index != -1:
        cart[index]['price'] = new_price
    return cart
