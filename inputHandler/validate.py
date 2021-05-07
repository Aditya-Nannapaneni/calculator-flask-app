
def validate_input(str_input):
    '''
    AIM: Checks validity if input string, conditions include: correct number of parantheses
         presence of unallowed characters, more that 2 operators in series,
         checks for the second operator to be a minus sign
         
    INPUT: raw arithmetic string to be  evaluated

    OUTPUT: valid  if the input string is valid else outputs invalid input
    '''
    ops = '+-/*'
    inputWithoutSpaces = str_input.replace(" ", "")
    allowedElements = "1234567890.()*/-+"
    parentheses_count = 0
    
    for i in range(len(inputWithoutSpaces)):
        if inputWithoutSpaces[i] == '(':
            parentheses_count += 1
        elif inputWithoutSpaces[i] == ')':
            parentheses_count -= 1
            if parentheses_count < 0:
                #problem with parentheses
                return 'invalid input'
            
        if inputWithoutSpaces[i] not in allowedElements:
            #wrong characcters in input
            return 'invalid input'
        
        if inputWithoutSpaces[i] in ops and i+1 < len(inputWithoutSpaces) and inputWithoutSpaces[i+1] in ops:
            if i+2 < len(inputWithoutSpaces) and inputWithoutSpaces[i+2] in ops:
                return 'invalid input'
            if inputWithoutSpaces[i+1] != '-':
                #problem with operators
                return 'invalid input'
        
        
        
    if parentheses_count != 0:
        #problem with parentheses
        return 'invalid input'
    
    return 'valid input'