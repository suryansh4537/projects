from tkinter import *

window=Tk()
pic1=PhotoImage(file="C:\\Users\\LENOVO\\Pictures\\b1.png")
pic11 = pic1
pic2=PhotoImage(file="C:\\Users\\LENOVO\\Pictures\\b3.png")
pic22 = pic2
def addCustomer():

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


c=Canvas(window,bg='red',width=1200,height=600)
pic=PhotoImage(file="C:\\Users\\LENOVO\\Pictures\\br.png")
background=Label(window,image=pic)
background.place(x=0,y=0,relwidth=1,relheight=1)



c.pack()
lab=Label(window,text="M",bg="black",fg="white",font=("ARIAL",35)).place(x=390,y=50)
lab=Label(window,text="A",font=("ARIAL",30)).place(x=440,y=45)
lab=Label(window,text="R",bg="black",fg="white",font=("ARIAL",35)).place(x=480,y=50)
lab=Label(window,text="K",font=("ARIAL",30)).place(x=520,y=45)
lab=Label(window,text="E",bg="black",fg="white",font=("ARIAL",35)).place(x=560,y=50)
lab=Label(window,text="T",font=("ARIAL",30)).place(x=600,y=45)
lab=Label(window,text="A",bg="black",fg="white",font=("ARIAL",35)).place(x=665,y=45)
lab=Label(window,text="P",font=("ARIAL",30)).place(x=705,y=50)
lab=Label(window,text="P",bg="black",fg="white",font=("ARIAL",35)).place(x=745,y=45)
b=Button(window,text="ADD CUSTOMER",bg="grey",bd=0,width=50,height=2,fg="white",command=addCustomer).place(x=420,y=200)
b=Button(window,text="UPDATE CUSTOMER",bg="grey",bd=0,width=50,height=2,fg="white").place(x=420,y=260)
b=Button(window,text="DELETE CUSTOMER",bg="grey",bd=0,width=50,height=2,fg="white").place(x=420,y=320)
b=Button(window,text="DETAILS OF CUSTOMER",bg="grey",bd=0,width=50,height=2,fg="white").place(x=420,y=380)

exit=Button(window,text="EXIT",bd=0,bg="black",fg="white",width="30",height=2,command=window.destroy).place(x=500,y=500)
window.mainloop()
