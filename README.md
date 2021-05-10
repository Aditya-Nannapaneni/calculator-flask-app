# Calculator Flask App

## Usage
The API's here are being consumed by a completely separate React App to serve the results of the calculator. Both the Flask and React API's aredeployed on Heroku and you can use the link below to access the live version.

    Link: https://calculator-ui-app.herokuapp.com/
    
## Constraints

     - Takes arithmetic expression in Infix Notation as input.
     - Positive, negative & decimal numbes are allowed.
     - Supports +, -, *, / operations.
     - Supports multiple levels of nested parantheses in the 

## Approach

  ### Algorithm:
  - The input infix arithmetic expression is first split into tokens.
  - The array containing tokens are cleaned, pre-processed.
  - The expression if converted into Postfix Notation.
  - Postfix expression is evaluated and result is obtained. 
  - Time Complexity: O(n), Space Complexity:  O(n), where n is the length of the input expression.

  
  ### Solution Architecture:
  As described above in the Algorithm section, various similar steps are grouped together into modules adhering to the DRY principle. The final list of modules used and a brief pourpose for each module is specified below:
  
  #### inputHandler:
  Module containing functions that check validity of the input provided. Cases where input is considered invalid:  Number of opening and closing parantheses don't match, input has characters not in the allowed set of elements (characters. that are not digits).
                   
  #### preprocessor:
  Module containg functions that split the input expression into tokens, fix potential issues with propagating minus sign, convert the infix expression to prostfix notation and evaluates the cleaned postfix notation.
  
  #### calculate:
  Module containing wrapper function that utilizes all the other modules to calculate the result.
  
  #### arithmeticOperations:
  Module containig function to compute the result of the arithmetic operation for 2 operands. Division by zero error is handled here.
  
  #### utils:
  Module containing functions that are frequently used by other functions.


  ### Other important files and folders:
  
  #### tests
  Folder containing all the tests. Tests can be run using the following command:  ```` $ coverage run -m unittest discover ````
  To generate a test coverage report use: ```` $ coverage report ````
  Current test coverage percentage:
  
  
  #### main.py
  
  



  
