from tkinter import *
import re

root=Tk()
root.title("Complex Calculator")

op=["+","-","*","/"]
history=[]

class calculator:

    @classmethod
    def Error(cls):
        if e.get()=="Invalid Syntax":
            e.delete(0,END)

    @classmethod
    def button_click(cls,n):
        calculator.Error()
        a=e.get()
        e.delete(0,END)
        if n in op:
            for i in op:
                if a.endswith(i):
                    a=f"{a[:-1]}{n}"
                    e.insert(0,a)
                    return
        e.insert(0, f"{a}{n}")

    @classmethod
    def button_decimal(cls):
        calculator.Error()
        a=e.get()
        e.delete(0,END)
        e.insert(0,f"{a}.")

    @classmethod
    def button_clear(cls):
        fnum=None
        snum=None
        s=None
        e.delete(0,END)

    @classmethod
    def button_backspace(cls):
        a=len(e.get())
        e.delete(a-1,END)

    @classmethod
    def button_equal(cls):
        fnum=e.get()
        history.append(fnum)
        while True:
            if match:=re.search(r"(\+|-|\*)?(\d+(\.\d+)?)/(\d+(\.\d+)?)(\+|-|\*)?",fnum):
                pattern = r"(\+|-|\*)?(\d+(\.\d+)?)/(\d+(\.\d+)?)(\+|-|\*)??"
                try:
                    divide=float(match.group(2))/float(match.group(4))
                except ZeroDivisionError:
                    e.delete(0,END)
                    e.insert(0,"Error")
                    return
                fnum=re.sub(pattern, lambda  match: f"{match.group(1) or ""}{divide}{match.group(6) or ""}",fnum,count=1)
            else:
                break

        while True:
            if match:=re.search(r"(\+|-|/)?(\d+(\.\d+)?)\*(\d+(\.\d+)?)(\+|-|/)?",fnum):
                pattern = r"(\+|-|/)?(\d+(\.\d+)?)\*(\d+(\.\d+)?)(\+|-|/)?"
                multiply=float(match.group(2))*float(match.group(4))
                fnum=re.sub(pattern, lambda  match: f"{match.group(1) or ""}{multiply}{match.group(6) or ""}",fnum,count=1)
            else:
                break

        while True:
            if match:=re.search(r"(\*|/)?(?!-)(\d+(\.\d+)?)\+(\d+(\.\d+)?)(\*|-|/)?",fnum):
                pattern = r"(\*|/)?(?!-)(\d+(\.\d+)?)\+(\d+(\.\d+)*)(\*|-|/)?"
                add=float(match.group(2))+float(match.group(4))
                fnum=re.sub(pattern, lambda  match: f"{match.group(1) or ""}{add}{match.group(6) or ""}",fnum,count=1)
                
            elif match:=re.search(r"(-)?(\d+(\.\d+)?)\+(\d+(\.\d+)?)(\*|-|/)?",fnum):
                pattern = r"(-)?(\d+(\.\d+)?)\+(\d+(\.\d+)*)(\*|-|/)?"
                add=float(match.group(4))-float(match.group(2))
                if add<0:
                    fnum=re.sub(pattern, lambda  match: f"{match.group(1) or ""}{add}{match.group(6) or ""}",fnum,count=1)
                else:
                    fnum=re.sub(pattern, lambda  match: f"+{add}{match.group(6) or ""}",fnum,count=1)
            else:
                break

        while True:
            if match:=re.search(r"(|\*|/)?(?!\+)(\d+(\.\d+)?)-(\d+(\.\d+)?)(\+|\*|/)?",fnum):
                pattern = r"(\+|\*|/)?(?!\+)(\d+(\.\d+)?)-(\d+(\.\d+)?)(\+|\*|/)?"
                sub=float(match.group(2))-float(match.group(4))
                fnum=re.sub(pattern, lambda  match: f"{match.group(1) or ""}{sub}{match.group(6) or ""}",fnum,count=1)
            
            elif match:=re.search(r"(-)?(\d+(\.\d+)?)\+(\d+(\.\d+)?)(\*|-|/)?",fnum):
                pattern = r"(-)?(\d+(\.\d+)?)\+(\d+(\.\d+)*)(\*|-|/)?"
                sub=float(match.group(4))+float(match.group(2))
                fnum=re.sub(pattern, lambda  match: f"+{sub}{match.group(6) or ""}",fnum,count=1)

            else:
                break
        
        if match:=re.search(r"^(\+|-)?(\d+(\.\d+)?)$",fnum):
            e.delete(0,END)
            e.insert(0,fnum)
        else:
            e.delete(0,END)
            e.insert(0,"Invalid Syntax")
        
class simple_calculator(calculator):

    def __init__(self):
        global e 
        e=Entry(root ,width=35)
        e.grid(row=0,column=0,columnspan=3)
        
        button1=Button(root,text="1",padx=28,pady=17,command=lambda: calculator.button_click(1)).grid(row=1,column=0)
        button2=Button(root,text="2",padx=28,pady=17,command=lambda: calculator.button_click(2)).grid(row=1,column=1)
        button3=Button(root,text="3",padx=28,pady=17,command=lambda: calculator.button_click(3)).grid(row=1,column=2)
        button4=Button(root,text="4",padx=28,pady=17,command=lambda: calculator.button_click(4)).grid(row=2,column=0)
        button5=Button(root,text="5",padx=28,pady=17,command=lambda: calculator.button_click(5)).grid(row=2,column=1)
        button6=Button(root,text="6",padx=28,pady=17,command=lambda: calculator.button_click(6)).grid(row=2,column=2)
        button7=Button(root,text="7",padx=28,pady=17,command=lambda: calculator.button_click(7)).grid(row=3,column=0)
        button8=Button(root,text="8",padx=28,pady=17,command=lambda: calculator.button_click(8)).grid(row=3,column=1)
        button9=Button(root,text="9",padx=28,pady=17,command=lambda: calculator.button_click(9)).grid(row=3,column=2)
        button0=Button(root,text="0",padx=28,pady=17,command=lambda: calculator.button_click(0)).grid(row=4,column=0)



        buttonadd=Button(root,text="+",padx=28,pady=17,command=lambda: calculator.button_click("+")).grid(row=5, column=0)
        buttonsub=Button(root,text="-",padx=29,pady=17,command=lambda: calculator.button_click("-")).grid(row=4, column=1)
        buttonmulti=Button(root,text="*",padx=28,pady=17,command= lambda: calculator.button_click("*")).grid(row=4, column=2)
        buttondiv=Button(root,text="/",padx=29,pady=17,command= lambda: calculator.button_click("/")).grid(row=6, column=0)
        buttonclear=Button(root,text="Clear",pady=18,padx=17,command=calculator.button_clear).grid(row=5,column=2)
        buttonbackspace=Button(root,text="<-",pady=18,padx=23,command=calculator.button_backspace).grid(row=5,column=1)
        buttondecimal=Button(root,text=".",pady=17,padx=28,command=calculator.button_decimal).grid(row=6,column=1)
        buttonequal=Button(root,text="=",command= calculator.button_equal,pady=17,padx=28).grid(row=6,column=2)
        root.mainloop()

#I am going to try and add more features like history however log and sin functions seem to be a bit tricky for now.         
'''        

class complex_calculator(calculator):
    def __init__(self):
        global e
        e=Entry(root,width=48)
        e.grid(row=0,column=0,columnspan=4)
        

        button1=Button(root,text="1",padx=28,pady=17,command=lambda: calculator.button_click(1)).grid(row=1,column=1)
        button2=Button(root,text="2",padx=28,pady=17,command=lambda: calculator.button_click(2)).grid(row=1,column=2)
        button3=Button(root,text="3",padx=28,pady=17,command=lambda: calculator.button_click(3)).grid(row=1,column=3)
        button4=Button(root,text="4",padx=28,pady=17,command=lambda: calculator.button_click(4)).grid(row=2,column=1)
        button5=Button(root,text="5",padx=28,pady=17,command=lambda: calculator.button_click(5)).grid(row=2,column=2)
        button6=Button(root,text="6",padx=28,pady=17,command=lambda: calculator.button_click(6)).grid(row=2,column=3)
        button7=Button(root,text="7",padx=28,pady=17,command=lambda: calculator.button_click(7)).grid(row=3,column=1)
        button8=Button(root,text="8",padx=28,pady=17,command=lambda: calculator.button_click(8)).grid(row=3,column=2)
        button9=Button(root,text="9",padx=28,pady=17,command=lambda: calculator.button_click(9)).grid(row=3,column=3)
        button0=Button(root,text="0",padx=28,pady=17,command=lambda: calculator.button_click(0)).grid(row=4,column=1)

        buttonadd=Button(root,text="+",padx=28,pady=17,command=lambda: calculator.button_click("+")).grid(row=5, column=1)
        buttonsub=Button(root,text="-",padx=29,pady=17,command=lambda: calculator.button_click("-")).grid(row=4, column=2)
        buttonmulti=Button(root,text="*",padx=28,pady=17,command= lambda: calculator.button_click("*")).grid(row=4, column=3)
        buttondiv=Button(root,text="/",padx=29,pady=17,command= lambda: calculator.button_click("/")).grid(row=6, column=1)
        buttonclear=Button(root,text="Clear",pady=18,padx=17,command=calculator.button_clear).grid(row=5,column=3)
        buttonbackspace=Button(root,text="<-",pady=18,padx=23,command=calculator.button_backspace).grid(row=5,column=2)
        buttondecimal=Button(root,text=".",pady=17,padx=28,command=calculator.button_decimal).grid(row=6,column=2)
        buttonequal=Button(root,text="=",command= calculator.button_equal,pady=17,padx=28).grid(row=6,column=3)
        buttonbracket1=Button(root,text="(",command= calculator.button_click("("),pady=17,padx=28).grid(row=1,column=0)
        buttonbracket2=Button(root,text=")",command= calculator.button_click(")"),pady=17,padx=28).grid(row=2,column=0)
        buttonpower=Button(root,text="^",command= calculator.button_click("^"),pady=17,padx=28).grid(row=3,column=0)
        buttonfactorial=Button(root,text="!",command= calculator.button_click(")"),pady=17,padx=28).grid(row=4,column=0)
        buttonpi=
        root.mainloop()
'''
x=simple_calculator()

