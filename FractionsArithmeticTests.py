#!/usr/bin/python3

import os, sys, unittest, math
import FractionsArithmetic as fa

class TestFractionsArithmetic(unittest.TestCase):

    def run_these(self, tests):
        for expression, expected_result in tests.items():
            self.assertEqual(fa.ASList(expression).compute(), expected_result)

    def test_001(self):
        """ Simple integer addition and subtraction """
        tests = {
            '1 + 1': '2',
            '2 + 1': '3',
            '1 + 2': '3',
            '0 + 0': '0',
            '0 + 1': '1',
            '111 + 222': '333',
            '10 + -10': '0',
            '1 + 2 + 3 + 4 + 5 - 14': '1',
            '1 + 2 + 3 + 4 + 5 - 15': '0',
            '1 + 2 + 3 + 4 + 5 - 16': '-1'
        }
        self.run_these(tests)

    def test_002(self):
        """ Addition and subtraction of mixed numbers """
        tests = {
            '2_3/8 + -19/8': '0',
            '1_1/4 + 1_1/4': '2_1/2',
            '1_1/4 - 1/2': '3/4',
            '1_1/3 + 2/3': '2',
            '1_1/8 + 1_1/8 + 1_1/8 + 1_1/8 + 1_1/8 + 1_1/8 + 1_1/8': '7_7/8',
            '     1_1/10       +    9/10    ': '2',
            '1/12345 + 1/67890 - 1783/18624490 + 1/2': '1/2'
        }
        self.run_these(tests)

    def test_003(self):
        """ Multiplication and division of whole numbers """
        tests = {
            '5 * 5': '25',
            '1 * 0': '0',
            '0 * 9': '0',
            '1 * 9': '9',
            '1 * 2 * 3 * 4 * 5': str(math.factorial(5)),
            '1 * 2 * -1 * 3 * 4 * 5': str(-math.factorial(5)),
            '-1 * -2 * -3 * -4': str(math.factorial(4)),
            '1 * 2 * 3 * 4 * 5 / 120': '1',
            '0 / 10': '0',
            '100 / 5 / -4 / 5 * 4': '-4'
        }
        self.run_these(tests)

    def tests_004(self):
        """ Operator precendence """
        tests = {
            '10 + 2 * 4 - 8': '10',
            '10_3/2 - 1/2 * 3 - 4_1/4': '5_3/4',
            '5 * 5 + 25 + 50 / 10 - 4_21/42': '50_1/2'
        }
        self.run_these(tests)

if __name__ == '__main__':
    unittest.main()

