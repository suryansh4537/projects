import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *

# Use the application default credentials
cred = credentials.Certificate("suryansh1-firebase-adminsdk-vpxcz-f3ad779206.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
"""
class abc:
    def __init__(self,name,phone,email,lp,uid):
        self.name=name
        self.phone=phone
        self.email=email
        self.lp=lp
        self.uid=uid

def add():
    cref=abc(None,None,None,None,None)
    cref.name=e1.get()
    cref.phone=e2.get()
    cref.email=e3.get()
    cref.lp=e4.get()
    cref.uid=e5.get()
    d1=cref.__dict__
    db.collection("Customer").document().set(d1)
    print("Added data in Firebase")


window=Tk()
l1=Label(window,text="Enter name=")
l1.pack()
e1=Entry(window)
e1.pack()
l1=Label(window,text="Enter phone=")
l1.pack()
e2=Entry(window)
e2.pack()
l1=Label(window,text="Enter email=")
l1.pack()
e3=Entry(window)
e3.pack()
l1=Label(window,text="Enter lp=")
l1.pack()
e4=Entry(window)
e4.pack()
l1=Label(window,text="Enter uid=")
l1.pack()
e5=Entry(window)
e5.pack()
b1=Button(window,text="add",command=add)
b1.pack()
"""
docs = db.collection("Customer").stream()

for doc in docs:
    print(doc.id, doc.to_dict())
#window.mainloop()

