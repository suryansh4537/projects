from tkinter import *
from tkinter import messagebox
from marketsimulator import *
import random
import mysql.connector
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="marketproject")
cursor = con.cursor()

db=dbHelper()


window=Tk()
window.geometry("1200x600")
window.resizable(0,0)
pic1=PhotoImage(file="C:\\Users\\LENOVO\\Videos\\Captures\\G3.png")
pic11 = pic1
pic2=PhotoImage(file="C:\\Users\\LENOVO\\Pictures\\b3.png")
pic22 = pic2

def newCustomer():
    def popup(s,s1):
        messagebox.showinfo(s,s1)

    def add():

        cRef = customer(None, None, None, 100, None, 1)
        cRef.name=e1.get()
        cRef.phone=e2.get()
        cRef.email=e3.get()
        cRef.uid = random.randrange(1000,10000)
        if len(e1.get())==0:
            messagebox.showerror("Error","Name left Empty")
            win1.destroy

        elif len(e2.get())==0:
            messagebox.showerror("Error","Phone left Empty")
            win1.destroy

        elif len(e3.get())==0:
            messagebox.showerror("Error","Email left Empty")
            win1.destroy
        else:
            db.saveCustomerInDB(cRef)
            popup("ADDED",F"YOUR UID={cRef.uid}")
            win1.destroy



    win1=Toplevel(window)
    c=Canvas(win1,bg='red',width=900,height=400)

    background=Label(win1,image=pic11)
    background.place(x=0,y=0,relwidth=1,relheight=1)
    l1 = Label(win1, text="CUSTOMER DETAILS", fg="white",bg="black",font=(20)).place(x=330, y=20)
    l1=Label(win1,text="NAME",bg="grey",fg="black").place(x=90,y=80)
    e1=Entry(win1,width=100)
    e1.place(x=250,y=83)
    l1=Label(win1,text="PHONE",bg="grey",fg="black").place(x=90,y=140)
    e2=Entry(win1,width=100)
    e2.place(x=250,y=143)
    l1=Label(win1,text="EMAIL",bg="grey",fg="black").place(x=90,y=200)
    e3=Entry(win1,width=100)
    e3.place(x=250,y=203)
    b1 =Button(win1, text="ADD", bd=0, bg="black", fg="white", width="30", height=2, command=add).place(x=350,y=270)

    exit = Button(win1, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2, command=win1.destroy).place(x=350,y=330)
    c.pack()


def existingCustomer():

    def Continue():
        def update():
            cRef = customer(None, None, None, None, None, None)
            db.fetchCustomer(int(e1.get()))

        win1.destroy()
        win2 =Toplevel(window)

        c = Canvas(win2, bg='red', width=900, height=400)

        background = Label(win2, image=pic11)
        background.place(x=0, y=0, relwidth=1, relheight=1)

        l1 = Button(win2, text="UPDATE CUSTOMER",width=50,height=2, bg="PURPLE",bd=0, fg="WHITE").place(x=280, y=140)

        l1 = Button(win2, text="DELETE CUSTOMER",width=50,height=2, bg="PURPLE",bd=0, fg="WHITE").place(x=280, y=200)

        B3 = Button(win2, text="SHOPPING",width=50,height=2, bg="PURPLE",bd=0 ,fg="WHITE").place(x=280, y=260)

        b1 = Button(win2, text="Exit", bd=0, bg="black", fg="white", width="30", height=2, command=win2.destroy).place(x=350, y=330)

        c.pack()


    win1=Toplevel(window)
    c=Canvas(win1,bg='red',width=900,height=400)

    background=Label(win1,image=pic11)
    background.place(x=0,y=0,relwidth=1,relheight=1)
    lt = Label(win1, text="ENTER CUSTOMER ID", fg="white",bg="black",font=(20)).place(x=400, y=100)

    e1=Entry(win1,width=50)
    e1.place(x=370,y=190)
    B2 = Button(win1, text="CONTINUE", bd=0, bg="black", fg="white", width="30", height=2,command=Continue).place(x=350,y=270)

    exit = Button(win1, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2, command=win1.destroy).place(x=350,y=330)
    c.pack()


def showAll():
    win1=Toplevel(window)
    c=Canvas(win1,bg='red',width=900,height=400)

    background=Label(win1,image=pic11)
    background.place(x=0,y=0,relwidth=1,relheight=1)
    lt = Label(win1, text="CUSTOMER DETAILS", fg="white",bg="black",font=(20)).place(x=330, y=20)
    l1=Label(win1,text="NAME",bg="grey",fg="black",font=(14)).place(x=90,y=80)
    e1=Entry(win1,width=100).place(x=250,y=83)
    l1=Label(win1,text="PHONE",bg="grey",fg="black",font=(14)).place(x=90,y=140)
    e1=Entry(win1,width=100).place(x=250,y=143)
    l1=Label(win1,text="EMAIL",bg="grey",fg="black",font=(14)).place(x=90,y=200)
    e1=Entry(win1,width=100).place(x=250,y=203)
    l1=Label(win1,text="BOUGHT",bg="grey",fg="black",font=(14)).place(x=90,y=260)
    e1=Entry(win1,width=100).place(x=250,y=263)
    exit = Button(win1, text="EXIT", bd=0, bg="black", fg="white", width="30", height=2, command=win1.destroy).place(x=350,y=330)
    c.pack()



pic=PhotoImage(file="C:\\Users\\LENOVO\\Pictures\\br.png")
background=Label(window,image=pic1)
background.place(x=0,y=0,relwidth=1,relheight=1)




lab=Label(window,text="M",bg="black",fg="white",font=("ARIAL",35)).place(x=390,y=50)
lab=Label(window,text="A",font=("ARIAL",30)).place(x=440,y=45)
lab=Label(window,text="R",bg="black",fg="white",font=("ARIAL",35)).place(x=480,y=50)
lab=Label(window,text="K",font=("ARIAL",30)).place(x=520,y=45)
lab=Label(window,text="E",bg="black",fg="white",font=("ARIAL",35)).place(x=560,y=50)
lab=Label(window,text="T",font=("ARIAL",30)).place(x=600,y=45)
lab=Label(window,text="A",bg="black",fg="white",font=("ARIAL",35)).place(x=665,y=45)
lab=Label(window,text="P",font=("ARIAL",30)).place(x=705,y=50)
lab=Label(window,text="P",bg="black",fg="white",font=("ARIAL",35)).place(x=745,y=45)
b=Button(window,text="NEW CUSTOMER",bg="sky blue",bd=0,width=50,height=2,fg="black",command=newCustomer).place(x=420,y=240)
b=Button(window,text="EXISTING CUSTOMER",bg="sky blue",bd=0,width=50,height=2,fg="black",command=existingCustomer).place(x=420,y=300)
b=Button(window,text="SHOW ALL CUSTOMERS",bg="sky blue",bd=0,width=50,height=2,fg="black",command=showAll).place(x=420,y=360)

exit=Button(window,text="EXIT",bd=0,bg="black",fg="white",width="30",height=2,command=window.destroy).place(x=500,y=500)
window.mainloop()
