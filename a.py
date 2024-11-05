from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Black Hole")
#root.geometry("500X300")

upload = Image.open("image_3.jpg")
image = ImageTk.PhotoImage(upload)

label = Label(root, image= image, width=400, height= 300)
label.place(x=30, y=0)

label_1 = Label(root, text="This is an image of a real black hole.")
label_1.place(x=20, y=360)

root.mainloop()