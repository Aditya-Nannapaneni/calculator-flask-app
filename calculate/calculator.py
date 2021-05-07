# importing necessary functions
from inputHandler.validate import validate_input
from preprocessor.splitIntoTokens import get_token_array
from preprocessor.fixers import parantheses_multiplication_fixer
from preprocessor.fixers import minus_sign_fixer
from preprocessor.infixToPostfix import convertopostfix
from preprocessor.evalutatePostfixExpression import postfix_eval


def calculate_string_expression(arithmetic_expression):
    '''
    AIM: Validates, pre-processess, and evaluates the  input expression

    INPUT: Arithmetic expression to be evaluated

    OUTPUT: Result of the arithmetic expression if valid expression or says invalid expression
    '''
    in_str = arithmetic_expression['expression']

    if validate_input(in_str) == 'valid input':
        token_array = get_token_array(in_str)
        parantheses_fixed = parantheses_multiplication_fixer(token_array)
        negative_fixed = minus_sign_fixer(parantheses_fixed)
        postfix = convertopostfix(negative_fixed)
        return postfix_eval(" ".join(postfix))
    
    else:
        return 'invalid input'