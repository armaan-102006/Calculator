from tkinter import *

root=Tk()
n=0
def noclicks():
    global n
    while True:
        n+=1
        count=Label(root, text=f"You clicked {n} times.")
        count.pack()


button=Button(root,text="Click",command= noclicks)
button.pack()
root.mainloop()