def get_token_array(str_input):
    '''
    AIM: split the string input into an array of tokens

    INPUT: arithmetic expression in string format

    OUTPUT: input string split into an array  of tokens 
    '''
    ops = '*/-+()'
    inputWithoutSpaces = str_input.replace(" ", "")
    input_arr = [c for c in inputWithoutSpaces]
    token_arr = []
    i = 0
    while i < len(input_arr):
        cur = input_arr[i]
        if cur in ops:
            token_arr.append(cur)
        else:
            while i < len(input_arr)-1 and input_arr[i+1] not in ops:
                if cur == '.' and input_arr[i+1] == '.':
                    return "invalid input"
                cur += input_arr[i+1]
                i += 1

            if cur[-1] == '.':
                return "invalid input"

            token_arr.append(cur)
        i += 1

    return token_arr