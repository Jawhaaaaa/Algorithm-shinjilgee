import unittest

def count_primes(n: int) -> int:
    if n < 2:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return sum(is_prime)  

class TestCountPrimes(unittest.TestCase):

    def test_count_primes(self):
        self.assertEqual(count_primes(0), 0)     
        self.assertEqual(count_primes(1), 0)     
        self.assertEqual(count_primes(2), 1)     
        self.assertEqual(count_primes(3), 2)     
        self.assertEqual(count_primes(10), 4)    
        self.assertEqual(count_primes(18), 7)    
        self.assertEqual(count_primes(20), 8)    
        self.assertEqual(count_primes(100), 25)   

if __name__ == '__main__':

    x = int(5)
    print(x)
    unittest.main()
