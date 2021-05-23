import unittest
from task import conv_num, my_datetime, conv_endian
import random
import time
import string


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
        input = ''.join(random.choices(string.ascii_letters + string.digits, k = random.randint(10, 15)))
        new_test = build_test_func(None, input, conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(input), new_test)

    for _ in range(generate):
        # Tests if conv_num returns none for a number containing 2 decimals
        num = random.randint(-10000000, 10000000)
        input, index = str(num), random.randint(1, len(str(num))-1)
        input = input[:index] + '..' + input[index:]
        new_test = build_test_func(None, input, conv_num, message)
        setattr(RandomTestCase, 'test_{}'.format(input), new_test)


if __name__ == '__main__':
    generate_tests_conv_num()
    unittest.main(verbosity=1)