from tkinter import *
import BinarTK
import decimalTK
#=====================================================================
win = Tk()
win.title("Binar&Decimal")
win.geometry("600x500")
win.minsize(620,500)
win.maxsize(620,500)
win.config(bg='white')


#=====================================================================
def info():
    info = Tk()
    info.title("Info")
    info.geometry("600x500")
    info.minsize(650,400)
    info.maxsize(650,400)
    info.config(bg='white')
    titre = Label(info,text="""CONVERTER
                Binary & Decimal """,font=('arial',25),bg='white',fg='black')
    titre.place(x=50,y=10)

    titre = Label(info,text="""this script was made by B.MOHAED AMINE it's was just for training
in python and learn more skills this was my third project, i spent almost 3 days of work in this script and i hope
to learn more and moer about programmation and languages(Java script,C++....)
i think this is first step of me in may my career in programming, So i don't know if someone will read this but if
you read this be sur that i have all my trust in you for supporting me
And Thank you

..............





<3""",font=('arial',9),bg='white',fg='black')
    titre.place(x=20,y=100)
    QUIT = Button(info, text="Quit",command=info.destroy)
    QUIT.place(x=300,y=300)
#=====================================================================

#=====================================================================
titre = Label(text='CONVERTER',font=('arial',25),bg='white',fg='black')
titre.place(x=210,y=10)

Titre = Label(text="""HELLO, IF you want to convert from decimal to binary choise the right one
    if you want to convert from binary to dicimal choise the left one""",font=('arial',11))
Titre.place(x=70, y=100)

by = Label(win, text="by Med Amine")
by.place(x=515, y=480)

decimal_button = Button(text="Decimal To Binary",command=decimalTK.decimal_to_binary)
decimal_button.place(x=150,y=200)

binary_button = Button(text="Binary To Decimal",command=BinarTK.binary_to_decimal)
binary_button.place(x=400,y=200)

QUIT = Button(win, text="Quit",command=quit)
QUIT.place(x=100,y=400)

INFO = Button(win, text="INFO",command=info)
INFO.place(x=50,y=400)

win.mainloop
