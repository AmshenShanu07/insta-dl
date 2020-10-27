#IMPORTS
from os import link
from tkinter import *
from script import load
from PIL import ImageTk,Image

#Variable
script=load
input_font = ('Verdana',15)
screen_font = ('Verdana',25)
btn_font = ('Verdana',15)
bg_color='black'
font_colour='white'




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
app.geometry('400x490')
app.title('Insta-dl')
app.iconbitmap('script\\img\icon.ico')
app.configure(background=bg_color)
option=IntVar()
option.set(1)
btn=PhotoImage(file='script\\img\\btn.png')
img=Image.open('script\\img\\title.png')
bg=ImageTk.PhotoImage(img)

#title
Label(app,text='ver 1.0',fg='white',bg=bg_color,justify='center').grid(row=0,column=0)
title =Label(image=bg,bd=0)  
title.grid(column=0,row=1,pady=15)

#url entry
link=StringVar()
Label(app,text='URL',fg='white',bg=bg_color).grid(row=2,column=0,sticky=W,padx=50)
link=Entry(app,bd=1,font=input_font)
link.grid(row=2,column=0)

#radio buttons
radio_post=Radiobutton(app,variable=option,value=1,text='Post',fg=font_colour
                        ,bg=bg_color,activebackground=bg_color,activeforeground=bg_color,selectcolor=bg_color,font=10)
radio_pro_pic=Radiobutton(app,variable=option,value=2,text='porfile pic',fg=font_colour,bg=bg_color,
                            activebackground=bg_color,activeforeground=bg_color,font=10,selectcolor=bg_color)
radio_pro_pic.grid(row=4,column=0,sticky=E,padx=100,pady=10)
radio_post.grid(row=4,column=0,sticky=W,padx=100,pady=10)

#download button
download_btn=Button(app,image=btn,background=bg_color,activebackground=bg_color,bd=0 ,command=lambda:get())
download_btn.grid(row=5,column=0,pady=10)
banner=Entry(app,font=screen_font,bg=bg_color,bd=0,fg=font_colour,textvariable=script.result,justify='center')
banner.grid(row=6,column=0,pady=20)
banner.insert(0,script.result)

#result
Label(app,text='© AmshenShanu & AbirHasan & Palahsu',fg='white',bg=bg_color,justify='center').grid(row=7,column=0)
Label(app,text='Tool to download videos and photos from instagram',fg='white',bg=bg_color,justify='center').grid(row=8,column=0)


app.mainloop()