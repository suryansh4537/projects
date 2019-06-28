import random

import mysql.connector

con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="banana")

cursor = con.cursor()

class dbHelper():


    def saveCustomerInDB(self,customer):

        sql = f"insert into project1 values(null, '{customer.name}', '{customer.phone}', '{customer.email}',{customer.loyalty_pts},{customer.uid})"

        cursor.execute(sql)

        con.commit()

        print("details of customer saved!!!!!!!!")


    def updateCustomerInDB(self,customer):

        sql = f"update project1 set Name = '{customer.name}', email = '{customer.email}', Phone = '{customer.phone}' where uid = {uid}"


        cursor.execute(sql)

        con.commit()

        print("details of customer UPDATED!!!!!!!!")

    def deleteCustomerInDB(self, uid):
        sql = f"delete from project1 where uid = {uid}"

        cursor.execute(sql)

        con.commit()

        print(f"details of customerID {uid} Deleted!!!!!!!!")

    def fetchAllCustomers(self):

        sql = "select * from project1 order by name desc"

        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)

    def updatelp(self,abc):

        sql="update project1 set lp={}".format(abc.lp)
        cursor.execute(sql)
        con.commit()

    def fetchCustomer(self, uid):
        sql = "select * from project1 where uid = {}".format(uid)
        cursor.execute(sql)

        row = cursor.fetchone()
        print(row)



class customer():
    def __init__(self, name, phone, email, lp,uid):
        self.name = name
        self.phone = phone
        self.email = email
        self.lp = lp
        self.uid = uid

    def showCustomerDetails(self):
        print(f"Name  : {self.name}")
        print(f"Phone : {self.phone}")
        print(f"Email : {self.email}")
        print(f"UID =   {self.uid}")

print("1.  Add Customer Details!!!")

print("2. Already a Customer!!!")

print("3. Show all customers")

choice = int(input("Enter your Choice : "))
cost=0
lp1="select lp from project1 "
if choice == 1:

    cRef = customer(None, None,None,100,None)
    cRef.name = input("Enter name of the customer : ")
    cRef.phone = input("Enter phone of the customer : ")
    cRef.email = input("Enter email of the customer : ")
    cRef.uid = random.randrange(1000,10000)


    save = input("Do you want to save the details of the customer (yes/no): ")
    if save == "yes":

        db = dbHelper()
        db.saveCustomerInDB(cRef)
        print("*****CONGRATULATIONS YOU HAVE BEEN GIVEN 100 Loyalty Points*********")
        print("")
        cRef.showCustomerDetails()
        #loyalty points assign

#=========================================================================================
if choice == 2:
    uid = int(input("Enter your unique Customer id : "))
    print("1.  Update Customer Details!!")
    print("2. Delete the customer Details")
    print("3. Shopping")


    second_choice = int(input("Enter your Second Choice: "))



    if second_choice == 1:
        db = dbHelper()

        cRef = customer(None, None, None,None,None)
        db.fetchCustomer(uid)
        cRef.name = input("Enter name of the customer : ")
        cRef.phone = input("Enter phone of the customer : ")
        cRef.email = input("Enter email of the customer : ")

        save = input("Do you want to update the details (yes/no): ")
        if save == "yes":
            db = dbHelper()
            db.updateCustomerInDB(cRef)

    if second_choice == 2:

        save = input("Do you want to Delete the details (yes/no): ")
        if save == "yes":
            db = dbHelper()
            db.deleteCustomerInDB(uid)

    if second_choice == 3:
        lp1 = "select lp from project1 where uid='{}'".format(uid)
        cursor.execute(lp1)
        result=cursor.fetchone()
        r1=int(result[0])
        db = dbHelper()
        cRef = customer(None, None, None, r1, None)
        cost=int(input("Enter cost="))
        if cost>500 and cost<1000:
            cRef.lp=abs((10/100)*cost-int(cRef.lp))
            db.updatelp(cRef)
        elif cost>=1000:
            cRef.lp=abs()



if choice == 3:
    db = dbHelper()
    db.fetchAllCustomers()

