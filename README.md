# Calculator Flask App

## Usage
The API's here are being consumed by a completely separate React App to serve the results of the calculator. Both the Flask and React apps are deployed on Heroku and you can use the link below to access the live version!

    Link: https://calculator-ui-app.herokuapp.com/
    
Alternatively to run both the apps on your machine, please follow these steps:
- Clone both the calculator-flask-app and calculator-react-app repos.
- Open both the apps in an editor of your choice.
-  To start the react server use the command ```` $ yarn start ```` ,this will start the server on http://localhost:3000.
-  To start the flask server use the command ```` $ python main.py ```` ,this will start the server on http://0.0.0.0:9696/.
-  Navigate to App.js in the react app, on line 13 where we have to specify the url to send the POST request to change the existing url to http://0.0.0.0:9696/calculate to point it to the local flask server.
-  NOTE: You might have to install all the required pacakages, for the flask app use ```` $ pip install [package name] ````,  for the react app use                   ```` $ npm install [package name] ````.
-  You are now all set to use the app!!
    
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
  Module containing functions that check validity of the input provided. Cases where input is considered invalid:  Number of opening and closing parantheses don't match, input has characters not in the allowed set of elements (characters that are not digits).
                   
  #### preprocessor:
  Module containg functions that split the input expression into tokens, fix potential issues with propagating minus sign, convert the infix expression to postfix notation and evaluates the cleaned postfix notation.
  
  #### calculate:
  Module containing wrapper function that utilizes all the other modules to calculate the result.
  
  #### arithmeticOperations:
  Module containing  function to compute the result of the arithmetic operation for 2 operands. Division by zero error is handled here.
  
  #### utils:
  Module containing functions that are frequently used by other functions.


  ### Other important files and folders:
  
  #### tests
  Folder containing all the tests. 
  - Tests can be run using the following command:  ```` $ coverage run -m unittest discover ````
  - To generate a test coverage report use: ```` $ coverage report ````
  - Current test coverage percentage:
  ![](images/testcoverage.png)
  
  
  #### main.py
  File that has the POST request route, that takes in JSON data and evaluates the expression.
  
  



  
