import unittest
from InventoryAllocator import allocation

class Test(unittest.TestCase):

    def test_order_from_one_warehouse(self):
        order = {'apple': 1}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        self.assertEqual(output,allocation(order,inventory_distribution))
    
    def test_order_from_multiple_warehouse(self):
        order = { 'apple': 10 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        output = [{'dm': {'apple': 5}}, {'owd': {'apple': 5}}]
        self.assertEqual(output,allocation(order,inventory_distribution))
    
    def test_not_enough_inventory(self):
        order = { 'apple': 1 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
        output = []
        self.assertEqual(output,allocation(order,inventory_distribution))

    def test_multiple_items_multiple_warehouses(self):
        order = { 'apple': 5, 'banana': 5, 'orange': 5 }
        inventory_distribution = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]
        output = [{'dm': {'banana': 5}}, {'owd': {'apple': 5}}, {'owd': {'orange': 5}}]
        self.assertEqual(output,allocation(order,inventory_distribution))

    def test_empty_inventory_distribution(self):
        order = { 'apple': 15 }
        inventory_distribution = []
        output = []
        self.assertEqual(output,allocation(order,inventory_distribution))

    def test_order_available_from_multiple_prefer_single_warehouse(self):
        order = { 'apple': 15 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 20 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        output = [{'owd': {'apple': 15}}]
        self.assertEqual(output,allocation(order,inventory_distribution))
    
    def test_item_not_in_warehouse(self):
        order = { 'orange': 10 }
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 10 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        output = []
        self.assertEqual(output,allocation(order,inventory_distribution))
    

    def test_order_greater_than_inventory(self):
         order = { 'orange': 20 }
         inventory_distribution = [{ 'name': 'owd', 'inventory': { 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'orange': 5 }}]
         output = []
         self.assertEqual(output,allocation(order,inventory_distribution))
    
    def test_empty_order(self):
        order={}
        inventory_distribution = [{ 'name': 'owd', 'inventory': { 'apple': 10 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
        output = []
        self.assertEqual(output,allocation(order,inventory_distribution))

    def  test_one_item_available_other_not_availabel(self):
        order = { 'apple': 5, 'banana': 10 }
        inventory_distribution = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]
        output = []
        self.assertEqual(output,allocation(order,inventory_distribution))

if __name__ == '__main__':
    unittest.main()
