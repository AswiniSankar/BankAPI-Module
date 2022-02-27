# banking API using Rest methods
from flask import Flask, jsonify
import os

app = Flask(__name__)
# creating dummy data base
#here index is taken as customer id
customers = [{'Name': "Sandiya K",
              'Customer_ID': 90,
              'Account_Number': 78257192912,

              'Account_Type': "Savings",
              'Current_Balance': 20000
              },
             {'Name': "Praveen T",
              'Customer_ID': 28,
              'Account_Number': 78219192909,
              'Account_Type': "Current",
              'Current_Balance': 33900
              }
             ]


# to display all customers
@app.route('/customers', methods=['GET'])
def get():
    return jsonify({'Customers': customers})


# to display a particular customer based on customer id
@app.route('/customers/<int:C_ID>', methods=['GET'])
def get_id(C_ID):
    return jsonify({'Customers': customers[C_ID]})


# to create a new customer- this can be achived by using curl command
@app.route('/customers/create', methods=['POST'])
def create():
    customer = {'Name': "Mani V",
                'Customer_ID': 45,
                'Account_Number': 12257192912,

                'Account_Type': "Savings",
                'Current_Balance': 10000
                }

    customers.append(customer)
    return jsonify({'Created': customer})


# to update exiting customers account type
@app.route('/customers/update/<int:c_id>', methods=['PUT'])
def update(c_id):
    if customers[c_id]['Account_Type'] == "Current":
        customers[c_id]['Account_Type'] = "Savings"
    else:
        customers[c_id]['Account_Type'] = "Current"
    return jsonify({"customer": customers[c_id]})


# to delete the exiting customer by using customer id
@app.route('/customers/delete/<int:c_id>', methods=['DELETE'])
def delete(c_id):
    customers.remove(customers[c_id])
    return jsonify({'result': True})
# to deposite amount
@app.route('/customers/<int:c_id>/banking/deposite/<int:amount>', methods=['PUT'])
def deposite(c_id, amount):
    customers[c_id]['Current_Balance'] = customers[c_id]['Current_Balance'] + amount
    return jsonify({"Customer": customers[c_id]})


# to withdraw amount
@app.route('/customers/<int:c_id>/banking/withdrawal/<int:amount>', methods=['PUT'])
def withdraw(c_id, amount):
    if customers[c_id]['Current_Balance'] > amount:
        customers[c_id]['Current_Balance'] = customers[c_id]['Current_Balance'] - amount
        return jsonify({"Customer": customers[c_id]})
    else:
        return "insufficient fund"

port = os.environ.get("PORT",5000)  
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0.", port=port)
