from utils.checkStringIsFloat import isfloat
from arithmeticOperations.operations import doMath

def postfix_eval(postfix_expression):
    '''
    AIM: Evaluates the postfix expression using a stack, in a single pass.

    INPUT: Array of tokens in postfix notation.

    OUTPUT: Result of the arithmetic expression
    '''
    stack = []
    operators = ["+","-","*","/","^"]
    items = postfix_expression.split()
    for i in items:
        if (isfloat(i)):
        	stack.append(i)
        if (i in operators):
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = doMath(str(i),float(operand1),float(operand2))
            stack.append(result)
    return stack.pop()