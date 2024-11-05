from tkinter import *

root = Tk()
root.title("Window 1")

label_1 = Label(root, text= "This is root window.")
label_1.pack()



top = Toplevel()
top.title("Window 2")

label_2 = Label(top, text= "This is top level window.")
label_2.pack()

top.mainloop()
root.mainloop()