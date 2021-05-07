import unittest
#inserting the appropriate path to avoid import errors
import sys, os
sys.path.insert(0, os.path.dirname('/Users/adityanannapaneni/Git Hub Projects/Calculator App/utils'))
from utils.checkStringIsFloat import isfloat

class Testcalculate_checkStringIsFloat(unittest.TestCase):
    def test_isfloat_float(self):
        """
        Testing calculate_string_expression against a valid input
        """
        input_string = '8.89'
        result = isfloat(input_string)
        self.assertEqual(result, True)
    
    def test_isfloat_int(self):
        """
        Testing calculate_string_expression against a valid input
        """
        input_string = '8'
        result = isfloat(input_string)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()