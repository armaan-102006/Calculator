from tkinter import *
import re

root=Tk()
root.title("Complex Calculator")
e=Entry(root,width=35)
e.grid(row=0,column=0,columnspan=3)

import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

global s
global fnum
global snum
fnum=None
snum=None
s=None
def button_click(n):
    a=e.get()
    e.delete(0,END)
    e.insert(0, f"{a}{n}")

def button_decimal():
    a=e.get()
    e.delete(0,END)
    e.insert(0,f"{a}.")

def button_backspace():
    a=len(e.get())
    e.delete(a-1,END)

def button_add():
    global s 
    
    global fnum
    global snum
    
    if fnum is not None:
        snum=float(e.get())
        e.delete(0,END)
        fnum = ops[s](fnum, snum)

        s="+" 
        return fnum
    else:
        fnum=float(e.get())
        e.delete(0,END)
        s="+"

def button_sub():
    global s 
    
    global fnum
    global snum
    if fnum is not None:
        snum=float(e.get())
        e.delete(0,END)
        fnum = ops[s](fnum, snum) 
        s="-"
        return fnum
    else:
        fnum=float(e.get())
        s="-"
        e.delete(0,END)

def button_multi():
    global s 
    
    global fnum
    global snum
    if fnum is not None:
        snum=float(e.get())
        e.delete(0,END)
        fnum = ops[s](fnum, snum) 
        s="*"
        return fnum
    else:
        fnum=float(e.get())
        e.delete(0,END)
        s="*"

def button_div():
    global s 
    
    global fnum
    global snum
    if fnum is not None:
        snum=float(e.get())
        e.delete(0,END)
        fnum = ops[s](fnum, snum) 
        s="/"
        return fnum
    else:
        fnum=float(e.get())
        e.delete(0,END)
        s="/"

def button_equal():
    global s
    global fnum
    global snum
    
    snum=float(e.get())
    e.delete(0,END)
    if s=="+":
        result=fnum+snum
        e.insert(0,result)
    
    if s=="-":
        e.insert(0,fnum-snum)

    if s=="*":
        e.insert(0,fnum*snum)
    
    if s=="/":
        try:
            e.insert(0,fnum/snum)
        except ZeroDivisionError:
            e.insert(0,"Error")
    fnum=None
    snum=None
    s=None


def button_clear():
    fnum=None
    snum=None
    s=None
    e.delete(0,END)

button1=Button(root,text="1",padx=28,pady=17,command=lambda: button_click(1)).grid(row=1,column=0)
button2=Button(root,text="2",padx=28,pady=17,command=lambda: button_click(2)).grid(row=1,column=1)
button3=Button(root,text="3",padx=28,pady=17,command=lambda: button_click(3)).grid(row=1,column=2)
button4=Button(root,text="4",padx=28,pady=17,command=lambda: button_click(4)).grid(row=2,column=0)
button5=Button(root,text="5",padx=28,pady=17,command=lambda: button_click(5)).grid(row=2,column=1)
button6=Button(root,text="6",padx=28,pady=17,command=lambda: button_click(6)).grid(row=2,column=2)
button7=Button(root,text="7",padx=28,pady=17,command=lambda: button_click(7)).grid(row=3,column=0)
button8=Button(root,text="8",padx=28,pady=17,command=lambda: button_click(8)).grid(row=3,column=1)
button9=Button(root,text="9",padx=28,pady=17,command=lambda: button_click(9)).grid(row=3,column=2)
button0=Button(root,text="0",padx=28,pady=17,command=lambda: button_click(0)).grid(row=4,column=0)

buttonadd=Button(root,text="+",padx=28,pady=17,command=button_add).grid(row=5, column=0)
buttonsub=Button(root,text="-",padx=29,pady=17,command=button_sub).grid(row=4, column=1)
buttonmulti=Button(root,text="*",padx=28,pady=17,command= button_multi).grid(row=4, column=2)
buttondiv=Button(root,text="/",padx=29,pady=17,command= button_div).grid(row=6, column=0)
buttonclear=Button(root,text="Clear",pady=18,padx=17,command=button_clear).grid(row=5,column=2)
buttonbackspace=Button(root,text="<-",pady=18,padx=23,command=button_backspace).grid(row=5,column=1)
buttondecimal=Button(root,text=".",pady=17,padx=28,command= button_decimal).grid(row=6,column=1)
buttonequal=Button(root,text="=",command= button_equal,pady=17,padx=28).grid(row=6,column=2)

root.mainloop()