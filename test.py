from tkinter import *
from script import load
from PIL import ImageTk,Image

app=Tk()
img=Image.open('script\\title.png')
bg=ImageTk.PhotoImage(img)

Label(image=bg).place(x=0,y=0)
app.mainloop()