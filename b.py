from tkinter import *
from tkinter import messagebox

root = Tk()

def msg():
    messagebox.showwarning('Alert','Virus Detected')

b1 = Button(root, text= "Scan for virus", command= msg)
b1.place(x= 40, y = 80)

root.mainloop()