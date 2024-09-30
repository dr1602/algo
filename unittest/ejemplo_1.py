# Funcion para calcular el factorial

import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
        
    # def test_factorial_positive(self):
    #     self.assertEqual(factorial(5), 120)
        
    # def test_factorial_negative(self):
    #     with self.assertRaises(ValueError):
    #         factorial(-1)
            
if __name__ == '__main__':
    unittest.main()

'''
E.E
======================================================================
ERROR: test_factorial_negative (__main__.TestFactorial)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/root/algo/unittest/tempCodeRunnerFile.py", line 20, in test_factorial_negative
    factorial(-1)
  File "/root/algo/unittest/tempCodeRunnerFile.py", line 9, in factorial
    return n * factorial(n - 1)
  File "/root/algo/unittest/tempCodeRunnerFile.py", line 9, in factorial
    return n * factorial(n - 1)
  File "/root/algo/unittest/tempCodeRunnerFile.py", line 9, in factorial
    return n * factorial(n - 1)
  [Previous line repeated 980 more times]
  File "/root/algo/unittest/tempCodeRunnerFile.py", line 6, in factorial
    if n == 0:
RecursionError: maximum recursion depth exceeded in comparison

======================================================================
ERROR: test_factorial_zero (__main__.TestFactorial)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/root/algo/unittest/tempCodeRunnerFile.py", line 13, in test_factorial_zero
    self.asserEqual(factorial(0), 1)
AttributeError: 'TestFactorial' object has no attribute 'asserEqual'

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (errors=2)


.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''