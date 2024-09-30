import unittest
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 12.566370614359172, places=2)
        
if __name__ == '__main__':
    unittest.main()
    
'''
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

'''
assertAlmostEqual: compara si dos valores flotantes sonaproximadamente
igaes hasta un cierto numero de decimales

'''