
from utils.checkStringIsFloat import isfloat

def parantheses_multiplication_fixer(token_arr):
    '''
    AIM: adds * before and after parantheses to make it easier for computing the expression.
         Example  cases:
            1. ['(', 'x', ')', '(', 'y', ')'] -> ['(', 'x', ')', '*', (', 'y', ')'] 
            2. ['x', '(', 'y', '-', 'z', ')'] -> ['x', '*', '(', 'y', '-', 'z', ')'] 
            3. ['(', 'x', '-', 'y', ')', 'z'] -> ['(', 'x', '-', 'y', ')','*', 'z']

    INPUT: array containing tokens in infix notation

    OUTPUT: array of tokens with * in appropriate places
    '''
    paren_fixed = []
    for i in range(len(token_arr)):
        #case1
        if token_arr[i] == ')' and i+1 < len(token_arr) and token_arr[i+1] == '(':
            paren_fixed.append(token_arr[i])
            paren_fixed.append("*")
        #case2
        elif token_arr[i] == "(" and i > 0 and token_arr[i-1].isdigit():
            paren_fixed.append("*")
            paren_fixed.append(token_arr[i])

        #case3
        elif token_arr[i] == ")" and i+1 < len(token_arr) and token_arr[i+1].isdigit():
            paren_fixed.append(token_arr[i])
            paren_fixed.append("*")

        else:
            paren_fixed.append(token_arr[i])

    return paren_fixed




def minus_sign_fixer(token_arr):
    '''
    AIM: Handles potential problems with - sign in the token array and makes it easier for our evaluating functions.
        Example  cases:
                1. ['x', '+', '-', '(', 'y', '+', 'z', ')'] -> ['x', '+', '-1','*', '(', 'y', '+', 'z', ')'] 
                2. ['x', '+', '-', '4'] -> ['x', '+', '-4']

    INPUT: array containing tokens in infix notation

    OUTPUT: array of tokens after handling -  sign cases 
    '''
    minus_sign_fixed = []
    i = 0
    while i < len(token_arr):
        if token_arr[i] == '-' and i+1 < (len(token_arr)) and token_arr[i+1] == '(':
            if i > 0 and (token_arr[i-1].isdigit() or isfloat(token_arr[i-1])):
                minus_sign_fixed.append('+')
                minus_sign_fixed.append('-1')
                minus_sign_fixed.append('*')
                i += 1

        if token_arr[i] == '-' and i+1 < len(token_arr) and (token_arr[i+1].isdigit() or isfloat(token_arr[i+1])):
            if i > 0 and (token_arr[i-1].isdigit() or isfloat(token_arr[i-1])) or token_arr[i-1] == ')':
                minus_sign_fixed.append('+')
            minus_sign_fixed.append('-' + str(token_arr[i+1]))
            i += 1

        else:
            minus_sign_fixed.append(token_arr[i])

        i += 1
    return minus_sign_fixed