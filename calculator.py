
from tkinter import *
root=Tk()
root.geometry("633x900")
root.wm_iconbitmap("ca.ico") #logo icon file
def upl():
    statusvar.set("Wecolme")
root.title("Calculater")
def click(event):
    global statusvar
    text=event.widget.cget("text")
    if text=="=":
        value=eval(statusvar.get())
        print(value)
        statusvar.set(value)
        screen.update()
        
    elif text=="C":
        statusvar.set("")
        screen.update()
    else:
        statusvar.set(statusvar.get()+text)
        



statusvar=StringVar()
statusvar.set("")
screen=Entry(root,textvariable=statusvar,width=50, font=('Arial 24'))
screen.pack(fill=X,ipadx=8,padx=10,pady=10,)
f=Frame(root)
b=Button(f,text="7",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.pack(side="left",padx=18,pady=12)
b.bind('<Button-1>',click)
b=Button(f,text="8",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f,text="9",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
f.pack()

f1=Frame(root)
b=Button(f1,text="4",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f1,text="5",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f1,text="6",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
f1.pack()
f2=Frame(root)
b=Button(f2,text="1",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f2,text="2",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f2,text="3",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
f2.pack()

f3=Frame(root)
b=Button(f3,text="C",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f3,text="=",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f3,text="/",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
f3.pack()
f4=Frame(root)
b=Button(f4,text="+",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f4,text="-",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
b=Button(f4,text="*",font="lucida 35 bold",bg="gray",padx="10",pady="10")
b.bind('<Button-1>',click)
b.pack(side="left",padx=18,pady=12)
f4.pack()
root.mainloop()
