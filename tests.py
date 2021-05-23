import unittest
from task import conv_num, my_datetime, conv_endian
import random
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


if __name__ == '__main__':
    unittest.main()
