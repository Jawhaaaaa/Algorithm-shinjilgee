import unittest
import math

def aggregate_cost(n):
    total_cost = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:
            total_cost += i
        else:
            total_cost += 1
    return total_cost / n  

class Stack:
    def __init__(self, k):
        self.stack = []
        self.k = k
        self.operations_count = 0
        self.backup_count = 0  

    def push(self, item):
        self.stack.append(item)
        self.operations_count += 1
        if self.operations_count % self.k == 0:
            self.backup_count += 1

    def pop(self):
        if self.stack:
            self.stack.pop()
        self.operations_count += 1
        if self.operations_count % self.k == 0:
            self.backup_count += 1

    def get_operations_count(self):
        return self.operations_count

    def get_backup_count(self):
        return self.backup_count



def transform_potential_function(original_potential, i, D0):
    return original_potential(i) - original_potential(D0)

class TestAggregateCost(unittest.TestCase):
    def test_aggregate_cost(self):
        n = 8
        result = aggregate_cost(n)
        expected = 2.375  
        self.assertAlmostEqual(result, expected, places=2)

class TestStackOperations(unittest.TestCase):
    def test_stack1(self):
        k = 5
        stack = Stack(k)

        for i in range(10):
            stack.push(i)
        for i in range(10):
            stack.pop()

        self.assertEqual(stack.get_operations_count(), 20)
        self.assertEqual(stack.get_backup_count(), 4)

    def test_stack2(self):
        k = 5
        stack = Stack(k)

        for i in range(2):
            stack.push(i)
        for i in range(2):
            stack.pop()

        self.assertEqual(stack.get_operations_count(), 4)
        self.assertEqual(stack.get_backup_count(), 0)

class TestPotentialFunctionTransformation(unittest.TestCase):
    def test_potential_function_transformation(self):
        original_potential = lambda i: i + 5
        D0 = 0
        transformed_potential_D0 = transform_potential_function(original_potential, D0, D0)
        transformed_potential_D1 = transform_potential_function(original_potential, 1, D0)

        self.assertEqual(transformed_potential_D0, 0)
        self.assertGreaterEqual(transformed_potential_D1, 0)


if __name__ == "__main__":
    unittest.main()
