from flask import Flask, jsonify, request
from service import get_addition

app = Flask(__name__)

'''
API CALL: 
----------
Request URL   :  http://localhost:4000/add
Request Method:  POST GET PUT DELETE 
Payload       :  {json format}

-> Install dependent libraries    > pip install -r requirements.txt
-> Deploy  the application        > python app.py
-> API call will be given by UI developer
-> Configure API call in Postman tool
-> Implement API/EndPoint at backend    


REQ: Sum of 2 numbers 
    Functional Analysis: Customer will give 2 numbers we should load it and give addition result 
    Technical Analysis : sum(n1,n2) return result 
    
    API CALL : 
    ------------
    Request URL   : http://localhost:4000/add
    Request Method: POST 
    Payload       : {"num1":10,"num2":20}
    
    Response: {"result": 30}
'''

@app.route("/")
def welcome_page():
    print("---Flask Application : Welcome Page---")
    return "Hello World."

@app.route('/add', methods=['GET','POST'])
def add_nums():
    '''
    1. Load data: json to dict
    2. Server validations
    3. Pass data to service layer
    4. Send final response to UI : dict to json
    '''
    print("---Controller Layer: Adding Numbers---")
    print("json data : ", request.json, type(request.json))
    data = request.json
    print("Customer Data : ", data)
    if data['num1'] < 0 or data['num2'] < 0:
        return "Invalid Data"
    output = get_addition(data['num1'], data['num2'])
    return jsonify({'result': output}), 200


if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
