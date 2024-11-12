import unittest

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)   
        self.assertEqual(fibonacci(1), 1)   
        self.assertEqual(fibonacci(5), 5)   
        self.assertEqual(fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()
