# BankAPI-Module

Assessment to create a Banking application which should perform all CURD operations using Flask.

Prerequisite are 
Python 3,
Flask 

Steps involved
 
     1.Dummy database is created with the name of “customers” . Each customer has their name, account number, account type and available balance.
     2. CRUD operations done by using REST methods, url for those methods are
            i) to retrieve the all customer details- http://localhost:5000/customers
            ii) to retrieve particular customer -  http://localhost:5000/customers/<int:C_ID>
            iii)to create a new customer- http://localhost:5000/customers/create
            iV)to update the customer detail -  http://localhost:5000/customers/update/<int:C_ID>
            V)to delete a particular id -  http://localhost:5000/customers/delete/<int:c_ID>
     3. This API also does banking operations such as deposit and withdrawal. 
               i) to deposit -  http://localhost:5000/customers/banking/deposite/<int:amount>
              ii) to withdraw- http://localhost:5000/customers/banking/withdrawal/<int:amount>


        







