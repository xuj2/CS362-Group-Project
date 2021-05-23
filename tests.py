import unittest
from task import conv_num, my_datetime, conv_endian
import random

import time
import string
import datetime


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

    # Test my_datetime with random inputs
    def test_datetime4(self):
        for i in range(100000):
            seconds = random.randint(1, 9999999999)
            date = datetime.datetime.\
                utcfromtimestamp(seconds).strftime('%m-%d-%Y')
            self.assertEqual(date, my_datetime(seconds), seconds)

    # Test conv_endian for 0
    def test_conv_endian1(self):
        self.assertEqual('0', conv_endian(0))

    # Test conv_endian for random positive values, big endian format
    def test_conv_endian2(self):
        for i in range(100000):
            decimal = random.randint(1, 99999)
            hex_num = hex(decimal)
            hex_num = hex_num[2:].upper()
            hex_result = ' '.join(hex_num[i:i + 2]
                                  for i in range(0, len(hex_num), 2))
            self.assertEqual(hex_result, conv_endian(decimal))

    # Test conv_endian for random negative values, big endian format
    def test_conv_endian3(self):
        for i in range(100000):
            decimal = random.randint(-99999, -1)
            hex_num = hex(decimal)
            hex_num = hex_num[0] + hex_num[3:].upper()

            hex_result = ' '.join(hex_num[i:i + 2]
                                  for i in range(0, len(hex_num), 2))
            self.assertEqual(hex_result, conv_endian(decimal))

    # Test conv_endian for incorrect/mistyped endian inputs
    def test_conv_endian4(self):
        self.assertIsNone(conv_endian(10, 'BIG'))
        self.assertIsNone(conv_endian(10, 'Big'))
        self.assertIsNone(conv_endian(10, 'LITTLE'))
        self.assertIsNone(conv_endian(10, 'Little'))
        self.assertIsNone(conv_endian(10, 'Small'))
        self.assertIsNone(conv_endian(10, 'SMALL'))


class RandomTestCase(unittest.TestCase):
    pass


def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def generate_tests_conv_num(generate=10000):
    # Generates test cases for conv_num
    message = 'Test case: {}, Expected: {}, Result: {}'
    for _ in range(generate):
        # Test conv_num for correct output of valid number strings
        num = random.randint(-10000000000000, 10000000000000)
        new_test = build_test_func(num, str(num), conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(str(num)), new_test)
    
    for _ in range(generate):
        # Test conv_num for correct output of valid floats
        num = random.uniform(-10000, 10000)
        new_test = build_test_func(num, str(num), conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(str(num)), new_test)

    for _ in range(generate):
        # Tests conv_num for correct output of valid hex
        num = random.randint(-1000000000000, 10000000000000)
        hex_num = hex(num)
        new_test = build_test_func(num, str(hex_num), conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(str(num)), new_test)
    
    for _ in range(generate):
        # Tests if conv_num returns none for random strings of numbers and letters
        # Maybe this should be changed? Possibility of getting an actual hex number exists
        test_input = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 15)))
        new_test = build_test_func(None, test_input, conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(test_input), new_test)

    for _ in range(generate):
        # Tests if conv_num returns none for a number containing 2 decimals
        num = random.randint(-10000000, 10000000)
        test_input, index = str(num), random.randint(1, len(str(num))-1)
        test_input = test_input[:index] + '..' + test_input[index:]
        new_test = build_test_func(None, test_input, conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(test_input), new_test)


if __name__ == '__main__':
    generate_tests_conv_num()
    unittest.main(verbosity=1)
