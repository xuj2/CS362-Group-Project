import unittest
from task import conv_num, my_datetime, conv_endian
import random
import time


class TestCase(unittest.TestCase):

    # Test my_datetime for 0 seconds
    def test_datetime1(self):
        self.assertEqual('01-01-1970', my_datetime(0))

    # Test my_datetime for leap year
    def test_datetime2(self):
        self.assertEqual('06-06-1972', my_datetime(76680000))

    # Test my_datetime for 2/29 during leap year
    def test_datetime3(self):
        self.assertEqual('02-29-1972', my_datetime(68212800))

class RandomTestCase(unittest.TestCase):
    pass

def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test

if __name__ == '__main__':
    unittest.main()
