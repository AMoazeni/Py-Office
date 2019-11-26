import unittest

def add(a,b):
  return a+b

class TestDemo(unittest.TestCase):
    """Example of how to use unittest in Jupyter. Functions must contain the word 'test'."""
    
    def test_pass(self):
        self.assertEqual(add(2,2), 4)

    def test_fail(self):
        self.assertEqual(add(2,2), 5)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)



