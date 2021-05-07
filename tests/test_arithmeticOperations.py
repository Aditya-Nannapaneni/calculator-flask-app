import unittest
#inserting the appropriate path to avoid import errors
import sys, os
sys.path.insert(0, os.path.dirname('/Users/adityanannapaneni/Git Hub Projects/Calculator App/arithmeticOperations'))
from arithmeticOperations.operations import doMath


class TestdoMath(unittest.TestCase):
    def test_doMath_add(self):
        """
        Testing the doMath add functionality
        """
        op, op1, op2 = '+', 1, 2
        result = doMath(op, op1, op2)
        self.assertEqual(result, 3)
    
    def test_doMath_substract(self):
        """
        Testing the doMath substract functionality
        """
        op, op1, op2 = '-', 5, 2
        result = doMath(op, op1, op2)
        self.assertEqual(result, 3)


    def test_doMath_multiply(self):
        """
        Testing the doMath substract functionality
        """
        op, op1, op2 = '*', 5, 2
        result = doMath(op, op1, op2)
        self.assertEqual(result, 10)
    
    def test_doMath_divide(self):
        """
        Testing the doMath divide functionality
        """
        op, op1, op2 = '/', 5, 2
        result = doMath(op, op1, op2)
        self.assertEqual(result, 2.5)


    # def test_doMath_divide(self):
    #     """
    #     Testing the doMath divide functionality
    #     """
    #     op, op1, op2 = '/', 5, 0
    #     result = doMath(op, op1, op2)
    #     self.assertEqual(result, float('inf'))


    
# unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    unittest.main()