#!/usr/bin/env python3
"""
write a unit test for the function calculateExpressionString() from the calc.py script
the unit test should test the function with the test cases from the test.py script
"""

import unittest
from sympy import sympify
from calc import calculateExpressionString



class TestCalc(unittest.TestCase):

    CASES = {
    "1 + 1",
    "2 - 1",
    "2 * 2",
    "4 / 2",
    "2 ^ 2",
    "1 + 1 + 1",
    "2 - 1 - 1",
    "2 * 2 * 2",
    "4 / 2 / 2",
    "2 ^ 2 ^ 2",
    "1 + 1 * 2",
    "2 - 1 * 2",
    "2 * 2 + 2",
    "4 / 2 + 2",
    "2 ^ 2 + 2",
    "1 + 1 * 2 ^ 2",
    "2 - 1 * 2 ^ 2",
    "2 * 2 + 2 ^ 2",
    "4 / 2 + 2 ^ 2",
    "2 ^ 2 + 2 * 2",
    "1 + 1 * 2 ^ 2 - 2",
    "2 - 1 * 2 ^ 2 + 2",
    "2 * 2 + 2 ^ 2 / 2",
    "4 / 2 + 2 ^ 2 * 2",
    "2 ^ 2 + 2 * 2 - 2",
    "1 + 1 * 2 ^ 2 - 2 / 2",
    "2 - 1 * 2 ^ 2 + 2 / 2",
    "2 * 2 + 2 ^ 2 / 2 * 2",
    "4 / 2 + 2 ^ 2 * 2 / 2",
    "2 ^ 2 + 2 * 2 - 2 / 2",
    "1 + 1 * 2 ^ 2 - 2 / 2 + 2",
    "2 - 1 * 2 ^ 2 + 2 / 2 - 2",
    "2 * 2 + 2 ^ 2 / 2 * 2 + 2",
    "1 + 1 * 2 ^ 2 - 2 / 2 + 2 * 2 ^ 2",
    "2 - 1 * 2 ^ 2 + 2 / 2 - 2 * 2 ^ 2",
    "2 * 2 + 2 ^ 2 / 2 * 2 + 2 * 2 ^ 2",
    "4 / 2 + 2 ^ 2 * 2 / 2 + 2 * 2 ^ 2",
    "2 ^ 2 + 2 * 2 - 2 / 2 + 2 * 2 ^ 2",
    "1 + 1 * 2 ^ 2 - 2 / 2 + 2 * 2 ^ 2 - 2",
}

    def test_calculateExpressionString(self):
        for case in self.CASES:
            self.assertEqual(calculateExpressionString(case), float(sympify(case))) 

if __name__ == '__main__':
    unittest.main()