import unittest

from OpenFile import OpenFile

class TestPyOffice(unittest.TestCase):
    """PyOffice Test Functions."""
    
    def test_OpenFile_local(self):
        local_path = '../csv/california_housing_test.csv'
        self.assertEqual(str(type(OpenFile(local_path))), "<class 'dict'>")

    def test_OpenFile_url(self):
        url_path = 'https://raw.githubusercontent.com/AMoazeni/PyOffice/master/CSV%20Data/googleplaystore.csv'
        self.assertEqual(str(type(OpenFile(url_path))), "<class 'dict'>")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=True)



