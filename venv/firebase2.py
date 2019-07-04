import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import  random
cred=credentials.Certificate("suryansh1-firebase-adminsdk-vpxcz-f3ad779206.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
class DBhelper:

    def addCustomer(self,cref):

        cref.Name=input("Enter name=")
        cref.Email=input("Enter Email=")
        cref.Phone=input("Enter Phone=")
        cref.lp=100
        cref.uid=random.randint(1000,9999)
        data=cref.__dict__
        db.collection("Customer").document("{}".format(cref.uid)).set(data)
        print("Data Added Succesfully\nYour uid={}".format(cref.uid))

    def updateCustomer(self,cref):
        cref.uid=input("Enter uid to update the customer=")
        cref.Name=input("Enter name=")
        cref.Phone=input("Enter phone=")
        cref.Email=input("Enter email=")
        cref.lp=100
        d1=db.collection("Customer").document("{}".format(cref.uid))
        data=cref.__dict__
        d1.update(data)
        print("Updated succesfully")

    def deleteCustomer(self,cref):
        cref.uid=input("Enter uid to be Deleted=")
        d1=db.collection("Customer").document("{}".format(cref.uid)).delete()
        print("Customer deleted")

    def manipulateLP(self,cRef,cost,uid):

        if cost >= 500 and cost < 1000:
            if cRef.lp >=100:
                cost = cost-100
                cRef.lp = cRef.lp-100
                db.updatelp(cRef,uid)
                return cost

            elif cRef.lp<100:
                cost = cost - cRef.lp
                cRef.lp=0
                db.updatelp(cRef,uid)
                return cost


        elif cost >= 1000:
            if cRef.lp >=100:
                cost = cost-100

                cRef.lp = cRef.lp-100 + (0.1*cost)

                db.updatelp(cRef)
                return cost

            elif cRef.lp<100:
                cost = cost - cRef.lp
                cRef.lp = 0  + (0.1*cost)
                db.updatelp(cRef,cid)
                return cost

    def fetchOne(self,cref):
        cref.uid=input("Enter uid to fetch=")
        d1=db.collection("Customer").where("uid","==",cref.uid).stream()

        for i in d1:
            print(i.to_dict())

    def showAll(self):

        d1=db.collection("Customer").stream()
        m=[]
        for i in d1:
            m.append(i.to_dict())

        for i in range(0,len(m)):
            print(m[i])

class Customer:
    def __init__(self,Name,Phone,Email,lp,uid):
        self.Name=Name
        self.Phone=Phone
        self.Email=Email
        self.lp=lp
        self.uid=uid

cref=Customer(None,None,None,None,None)
db1=DBhelper()
#db1.addCustomer(cref)
#db1.fetchOne(cref)
#db1.updateCustomer(cref)
#db1.deleteCustomer(cref)
#db1.showAll()
#cost=int(input("Enter cost="))
db1.fetchOne(cref)

