import unittest

def sum_freq(freq, i, j):
    return sum(freq[i:j+1])

def greedy_optimal_bst(keys, freq, i=0, j=None):
    if j is None:
        j = len(keys) - 1

    if i > j:
        return 0

    max_freq_index = max(range(i, j + 1), key=lambda x: freq[x])

    root_cost = sum_freq(freq, i, j)

    left_cost = greedy_optimal_bst(keys, freq, i, max_freq_index - 1)
    right_cost = greedy_optimal_bst(keys, freq, max_freq_index + 1, j)

    return root_cost + left_cost + right_cost

class TestGreedyOptimalBST(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(greedy_optimal_bst([5, 6], [17, 25]), 59)
        self.assertEqual(greedy_optimal_bst([10, 20, 30], [34, 8, 50]), 142)
        self.assertEqual(greedy_optimal_bst([1, 2, 3, 4], [10, 30, 20, 40]), 190)
        self.assertEqual(greedy_optimal_bst([1], [10]), 10)

    def test_edge_cases(self):
        self.assertEqual(greedy_optimal_bst([], []), 0) 
        self.assertEqual(greedy_optimal_bst([1], [5]), 5)  

if __name__ == '__main__':
    unittest.main()
