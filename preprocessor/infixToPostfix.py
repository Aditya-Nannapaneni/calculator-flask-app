
def convertopostfix(token_arr):
    '''
    AIM: covert token array in infix notation to postfix notation

    INPUT: array  of tokens in infix notation

    OUTPUT: array of tokens in postfix notation.
    '''
    ops = '*/-+()'
    precedence = {
    '(': 1,
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3
    }
    postfixArray = []
    operatorStack = []
    
    for token in token_arr:
        if token not in ops:
            postfixArray.append(token)
        elif token == '(':
            operatorStack.append(token)
        elif token == ')':
            cur = operatorStack.pop()
            while cur != '(':
                postfixArray.append(cur)
                cur = operatorStack.pop()
        else:
            while operatorStack and precedence[operatorStack[-1]] >= precedence[token]:
                postfixArray.append(operatorStack.pop())
            operatorStack.append(token)
    while operatorStack:
        postfixArray.append(operatorStack.pop())
    return postfixArray