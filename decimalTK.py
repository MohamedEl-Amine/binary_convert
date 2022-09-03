from tkinter import *
def decimal_to_binary():
    decimal = Tk()
    decimal.title("Decimal To Binar")
    decimal.geometry("600x500")
    decimal.minsize(300,500)
    decimal.maxsize(300,500)
    decimal.config(bg='white')




    def bin_real(z):
        L = []
        while z != 0:
            z = z / 2
            if z%1== 0:
                L+= [0]
                z = int(z)
            else:
                L+= [1]
                z = int(z)
        L.reverse()

        strings = [str(integer) for integer in L]
        a_string = "".join(strings)
        an_integer = int(a_string)
        
        binary_insert.insert(0,an_integer)
    #----------------------------------------
    def bin_unreal(z):
        f = z%1
        L = []
        F = []
        while z != 0:
            z = z / 2
            if z%1== 0:
                L+=[0]
                z = int(z)
            else:
                L+= [1]
                z = int(z)
        L.reverse()
        for i in range(4):
            f = f * 2
            if f >= 1:
                F += [1]
            else:
                F += [0]
            f = f%1
            
        strings = [str(integer) for integer in L]
        a_string = "".join(strings)
        an_integer = int(a_string)


        strings1 = [str(integer) for integer in F]
        a_string1 = "".join(strings1)
        an_integer1 = int(a_string1)

        Soll = an_integer1*(10)**(-4) 
        
        SOL = an_integer + Soll

        binary_insert.insert(0,SOL)
    #----------------------------------------
    def reset():
        binary_insert.delete(0, END)
        decimal_entry.delete(0, END)



    #----------------------------------------
    def Decimal_Full():
        if decimal_entry.get() =='':
            pass
        else:
            binary_insert.delete(0, END)
            global z
            z= float(decimal_entry.get())
            if z%1 == 0:
                bin_real(z)
            else:
                bin_unreal(z)
        




    #------------------------- Text
    B_To_D = Label(decimal,text="""DECIMAL
    TO
    BINARY""",font=('Corbel',34),bg='white')
    B_To_D.place(x=40,y=0)


    DECIMAL = Label(decimal,text="THE DECIMAL NUMBER",font=('Corbel',9),bg='white')
    DECIMAL.place(x=50,y=200)

    BINARY = Label(decimal,text="THE BAYNRY NUMBER",font=('Corbel',9),bg='white')
    BINARY.place(x=50,y=320)




    decimal_entry = Entry(decimal,font=('Corbel',10),bg='red')
    decimal_entry.place(x=50,y=230)


    CONVERTE = Button(decimal, text="convert",command=Decimal_Full)
    CONVERTE.place(x=50,y=275)


    binary_insert = Entry(decimal,font=('Corbel',10),bg='red')
    binary_insert.place(x=50,y=350)

    QUIT = Button(decimal, text="Quit",command=decimal.destroy)
    QUIT.place(x=50,y=400)

    reset = Button(decimal, text="Reset",command=reset)
    reset.place(x=100,y=400)


    #-------------------------------




    decimal.mainloop
