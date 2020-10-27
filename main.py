#IMPORTS
from os import link
from tkinter import *
from script import load
import tkinter
from PIL import ImageTk,Image

#Variable
script=load
input_font = ('Verdana',15)
screen_font = ('Verdana',25)
btn_font = ('Verdana',15)
bg_color='lightgrey'
font_colour='black'




#Functions
def get():
    url=link.get()
    select=option.get()
    
    if script.connection()==True:
        if select==1:
            script.download_post(url)
            banner.delete(0,END)
            banner.insert(0,script.result)
        elif select==2:
            script.download_pp(url)
            banner.delete(0,END)
            banner.insert(0,script.result)
    else:
        banner.delete(0,END)
        banner.insert(0,"No Internet")
            


#  G.U.I
app=Tk()
app.geometry('400x250')
app.title('InstaDownloader')
app.configure(background=bg_color)
option=IntVar()
option.set(1)
btn=PhotoImage(file='script\\btn.png')

#title
title = Label(app, text ='InstaDownloader', font = screen_font,fg=font_colour,bg=bg_color)  
title.grid(column=0,row=0)

#url entry
link=tkinter.StringVar()
link=Entry(app,bd=2,font=input_font)
link.grid(row=1,column=0)

#radio buttons
radio_post=Radiobutton(app,variable=option,value=1,text='Post',fg=font_colour,bg=bg_color,activebackground=bg_color,font=10)
radio_pro_pic=Radiobutton(app,variable=option,value=2,text='porfile pic',fg=font_colour,bg=bg_color,activebackground=bg_color,font=10)
radio_pro_pic.grid(row=2,column=0,sticky=E,padx=100)
radio_post.grid(row=2,column=0,sticky=W,padx=100)

#download button
download_btn=Button(app,image=btn,background=bg_color,activebackground=bg_color,bd=0 ,command=lambda:get())
download_btn.grid(row=3,column=0,pady=10)
banner=Entry(app,font=screen_font,bg=bg_color,bd=0,fg=font_colour,textvariable=script.result,justify='center')
banner.grid(row=4,column=0)
banner.insert(0,script.result)

#result
Label(app,text='©AmshenShanu & AbirHasan', bg=bg_color, justify='center').grid(row=5,column=0)



app.mainloop()