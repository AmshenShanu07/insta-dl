from os import link
from tkinter import *
from script import load
import tkinter


#Variable
script=load
input_font = ('Verdana',15)
screen_font = ('Verdana',25)
btn_font = ('Verdana',15)



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
            banner.delete(0,END)
            banner.insert(0,'Feature not added')
    else:
        banner.delete(0,END)
        banner.insert(0,"No Internet")
            




#  G.U.I
app=Tk()
app.geometry('425x230')
app.configure(background="orange")
app.title('InstaDownloader')
option=IntVar()
option.set(1)




title = Label(app, text ='InstaDownloader', font = screen_font,fg="#FF0055",bg='orange')  
title.grid(column=0,row=0)


link=tkinter.StringVar()
link=Entry(app,bd=4,font=input_font)
link.grid(row=1,column=0)

radio_post=Radiobutton(app,variable=option,value=1,text='Post',bg='orange',activebackground='orange')
radio_pro_pic=Radiobutton(app,variable=option,value=2,text='porfile pic',bg='orange',activebackground='orange')
radio_pro_pic.grid(row=2,column=0,sticky=E,padx=100)
radio_post.grid(row=2,column=0,sticky=W,padx=100)

download_btn=Button(text='Download' ,bg='red',fg='orange',width=10,height=2,font=btn_font,command=lambda:get())
download_btn.grid(row=3,column=0)
banner=Entry(app,font=screen_font,bg='orange',fg='white',textvariable=script.result,justify='center')
banner.grid(row=4,column=0)
banner.insert(0,script.result)

Label(app,text='©AmshenShanu&AbisHasan', bg='orange', justify='center').grid(row=5,column=0)


app.mainloop()