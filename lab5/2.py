import unittest

def knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

class TestKnapsack(unittest.TestCase):
    def test_case_1(self):
        wt = [1, 2, 3]
        val = [60, 100, 120]
        W = 5
        expected = 220
        self.assertEqual(knapsack(W, wt, val, len(wt)), expected)

    def test_case_2(self):
        wt = [1, 3, 4, 5]
        val = [10, 40, 50, 70]
        W = 7
        expected = 110
        self.assertEqual(knapsack(W, wt, val, len(wt)), expected)

    def test_case_3(self):
        wt = [5, 4, 6, 3]
        val = [10, 40, 30, 50]
        W = 10
        expected = 90
        self.assertEqual(knapsack(W, wt, val, len(wt)), expected)

if __name__ == "__main__":
    unittest.main()
