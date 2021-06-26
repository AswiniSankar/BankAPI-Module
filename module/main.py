#banking API using Restful
from flask import Flask, jsonify

app = Flask(__name__)
customers = [{'Name':"Sandiya K",

            'Account_Number': 78257192912,

            'Account_Type': "Savings",
             'Current_Balance': 20000
             },
     {'Name': "Praveen T",

             'Account_Number': 78219192909,
             'Account_Type': "Current",
             'Current_Balance': 33900
             }
            ]

@app.route('/customers', methods=['GET'])
def get():
    return jsonify({'Customers': customers})

@app.route('/customers/<int:C_ID>', methods=['GET'])
def get_id(C_ID):
    #if C_ID in customers:
    return jsonify({'customer': customers[C_ID]})

@app.route('/customers/create', methods=['POST'])
def create():
    customer ={'Name':"Mani V",

            'Account_Number': 12257192912,

            'Account_Type': "Savings",
             'Current_Balance': 10000
             }


    customers.append(customer)
    return jsonify({'Created': customer})
@app.route('/customers/update/<int:c_id>', methods=['PUT'])
def update(c_id):
    if   customers[c_id]['Account_Type'] == "Current":
        customers[c_id]['Account_Type'] = "Savings"
    else:
        customers[c_id]['Account_Type'] =  "Current"
    return jsonify({"couses": customers[c_id]})

@app.route('/customers/delete/<int:c_id>', methods=['DELETE'])
def delete(c_id):
    customers.remove(customers[c_id])
    return jsonify({'result': True})

@app.route('/customers/<int:c_id>/banking/deposite/<int:amount>', methods=['PUT'])
def deposite(c_id,amount):
    customers[c_id]['Current_Balance'] = customers[c_id]['Current_Balance'] +amount
    return jsonify({"Customer": customers[c_id]})
@app.route('/customers/<int:c_id>/banking/withdrawal/<int:amount>', methods=['PUT'])
def withdraw(c_id,amount):
    if  customers[c_id]['Current_Balance'] > amount:
        customers[c_id]['Current_Balance'] = customers[c_id]['Current_Balance'] - amount
        return jsonify({"Customer": customers[c_id]})
    else:
        return "insufficient fund"


if __name__ == "__main__":
    app.run(debug =True)


