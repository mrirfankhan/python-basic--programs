# Import module
from cProfile import label
from logging import PlaceHolder
from tkinter import *
def work():
    usern=userin.get()
    password=passvar.get()
    if usern=="admin" and password=="admin" :
        win = Toplevel(root)
        win.geometry("400x400")
        A=Label(win,text="Wrlcome admin panel",justify=CENTER,bg="red",font=("bold","15")).pack(pady=60)



#user=admin pass=admin enter defold login page

if __name__=="__main__":
    root = Tk()
    root.geometry("400x630")
    bg = PhotoImage( file = "bgimg.png")
    label1 = Label( root, image = bg)
    label1.place(x = 0,y = 0)
    userin=StringVar()
    passvar=StringVar()
    Label(root,text="Login now",font=("bold","25"),bg="red").pack(pady=20)
    fist1=Entry(root,textvariable=userin,font=("bold","14"))
    fist1.insert(0,"username")
    fist1.pack(pady=50)

    fist1=Entry(root,textvariable=passvar,font=("bold","14"))
    fist1.insert(0,"password")
    fist1.pack(padx=50)
    Button(root,text="Submint",width=7,bg="red",height=2,command=work).pack()
    root.mainloop()
