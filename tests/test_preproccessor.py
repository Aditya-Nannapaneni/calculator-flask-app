import unittest
#inserting the appropriate path to avoid import errors
import sys, os
sys.path.insert(0, os.path.dirname('/Users/adityanannapaneni/Git Hub Projects/Calculator App/preprocessor'))
from preprocessor.splitIntoTokens import get_token_array

class Testcalculate_get_token_array(unittest.TestCase):
    def test_calculate_string_expression_validInput(self):
        """
        Testing calculate_string_expression against a valid input
        """
        input_string_expression = "1+2(3)"
        result = get_token_array(input_string_expression)
        self.assertEqual(result, ['1', '+', '2', '(', '3', ')'])



if __name__ == '__main__':
    unittest.main()