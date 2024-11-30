import unittest

class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
        self.ratio = price / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.price
        else:
            total_value += item.ratio * capacity
            break
    
    return total_value

class TestFractionalKnapsack(unittest.TestCase):
    
    def test_full_items_fit(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        capacity = 60 
        result = fractional_knapsack(items, capacity)
        self.assertEqual(result, 280)
    
    def test_fractional_items(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        capacity = 50  
        result = fractional_knapsack(items, capacity)
        self.assertEqual(result, 240)
    
    def test_no_capacity(self):
        items = [Item(60, 10), Item(100, 20), Item(120, 30)]
        capacity = 0  
        result = fractional_knapsack(items, capacity)
        self.assertEqual(result, 0)
    
    def test_single_item(self):
        items = [Item(100, 50)]
        capacity = 10  
        result = fractional_knapsack(items, capacity)
        self.assertEqual(result, 20)
    
    def test_empty_item_list(self):
        items = []  
        capacity = 50
        result = fractional_knapsack(items, capacity)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
