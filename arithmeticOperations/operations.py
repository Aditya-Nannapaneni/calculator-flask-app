def doMath(op, op1, op2):
    '''
    AIM: Evaluates the operation to be done with the operands and returns the output.

    INPUT: Operation to  be done - (+, -, *, /), operands - (numbers, decimals)

    OUTPUT: Returns the  result after  performing the operation
    '''
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2