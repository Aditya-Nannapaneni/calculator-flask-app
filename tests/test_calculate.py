import unittest
#inserting the appropriate path to avoid import errors
import sys, os
sys.path.insert(0, os.path.dirname('/Users/adityanannapaneni/Git Hub Projects/Calculator App/calculate'))
from calculate.calculator import calculate_string_expression

class Testcalculate_string_expression(unittest.TestCase):
    def test_calculate_string_expression_validInput(self):
        """
        Testing calculate_string_expression against a valid input
        """
        arithmetic_expression = {'expression': '1+2'}
        result = calculate_string_expression(arithmetic_expression)
        self.assertEqual(result, 3)

    def test_calculate_string_expression_invalidInput(self):
        """
         Testing calculate_string_expression against an invalid input
        """
        arithmetic_expression = {'expression': '1+2++'}
        result = calculate_string_expression(arithmetic_expression)
        self.assertEqual(result, 'invalid input') 


if __name__ == '__main__':
    unittest.main()