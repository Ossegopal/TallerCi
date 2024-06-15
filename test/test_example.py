import os
import sys
import unittest

print(sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))))
from main import add_numbers

class TestAddition(unittest.TestCase):
    
    def test_add_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)
        
    def test_add_numbers_negative(self):
        result = add_numbers(-10, 5)
        self.assertEqual(result, -5)
        
if __name__ == '__main__':
    unittest.main()
