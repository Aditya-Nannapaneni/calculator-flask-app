#making necessary imports
from flask import Flask,  request, jsonify
from calculate.calculator import calculate_string_expression
from flask_cors import CORS

#instantiating our flask object
app = Flask("calculator_app")
CORS(app)


@app.route('/calculate', methods = ['POST'])
def calculate_expression():
    '''
    AIM: captures data from the POST request, evaluates the expression and returns a JSON output

    OUTPUT: JSON object containing the result of our arithematic expression
    '''
    input_expression_json = request.get_json()
    result  = calculate_string_expression(input_expression_json)
    response = {'result': result}

    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
