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

def generate_tests_conv_num(generate=5000):
    # Generates test cases for first function
    message = 'Test case: {}, Expected: {}, Result: {}'
    for _ in range(generate):
        num = random.randint(-10000000000000, 10000000000000)
        new_test = build_test_func(num, str(num), conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(str(num)), new_test)
    
    for _ in range(generate):
        num = random.uniform(-10000, 10000)
        new_test = build_test_func(num, str(num), conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(str(num)), new_test)

    for _ in range(generate):
        num = random.randint(-1000000000000, 10000000000000)
        hex_num = hex(num)
        new_test = build_test_func(num, str(hex_num), conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(str(num)), new_test)

    



if __name__ == '__main__':
    generate_tests_conv_num()
    unittest.main(verbosity=1)