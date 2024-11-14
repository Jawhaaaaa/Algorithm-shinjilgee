import unittest
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

class TestCoinChange(unittest.TestCase):
    
    def test_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
    
    def test_no_possible_change(self):
        self.assertEqual(coin_change([2], 3), -1)  
    
    def test_zero_amount(self):
        self.assertEqual(coin_change([1], 0), 0) 
    
    def test_other_cases(self):
        self.assertEqual(coin_change([1, 3, 4], 6), 2) 
        self.assertEqual(coin_change([5, 2, 1], 7), 2)  

if __name__ == "__main__":
    unittest.main()
