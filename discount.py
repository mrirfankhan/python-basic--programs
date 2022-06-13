from textwrap import fill
from tkinter import *
from turtle import bgcolor

from pyparsing import col

root=Tk()
def discount():
    global label2
    amount=varible.get()
    disc_price=varible1.get()
    amount1=(disc_price*amount)/100
    disc_price1=amount-amount1
    label3=Label(root,text=disc_price1,font="bold").grid(row=2,column=2)

    print(disc_price1)




root.geometry("300x300")
root.title("dicount clculator")
varible=IntVar()
varible1=IntVar()
# root.config(te)
labe1=Label(root,text="amount  ",font="Bold").grid(row=0)
labe1=Label(root,text="discount",font="Bold").grid(row=1)
label2=Label(root,text="discount is ",font="Bold").grid(row=2)
fast=Entry(root,textvariable=varible,font="bold",width=20).grid(row=0,column=2)
fast1=Entry(root,textvariable=varible1,font="bold",width=20).grid(row=1,column=2)
Button(text="Click ",bg="red", width=10,pady=5,command=discount).grid(row=4,column=2)
root.mainloop()
