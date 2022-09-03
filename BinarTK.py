from tkinter import *
def binary_to_decimal():
    binary = Tk()
    binary.title("Binar To Decimal")
    binary.geometry("600x500")
    binary.minsize(300,500)
    binary.maxsize(300,500)
    binary.config(bg='white')


    # Binar tO Decimal   -------------------------------
    def Binary_Full():
        global number, binar
        if binary_entry.get() =='':
            pass
        else:
            binar = binary_entry.get()[::-1]
            number = len(binar)
            decimal_insert.delete(0, END)
            if '.' in binar:
                Binar_R()
            else:
                Binar_N()
    ####################################################


    def Binar_N():
        solution = 0
        for i in range(0,number):
            if binar[i] == "1":
                solution = 2**i + solution   
            else:
                solution = 0 + solution
        decimal_insert.insert(0,solution)

    def Binar_R():
        for d in range(number):
            if binar[d] == ".":
                number_reel = d
                break

        solution = 0
        n = number_reel-1
        
        
            
        for i in range(n+1):
            if binar[i] == "1":
                solution = 2**n + solution
                n = n-1
            else:
                solution = 0 + solution
                n = n-1
                #### Second sol
        f = 1*(-1)
        n = number_reel-1
        for i in range(n+2,number):
            if binar[i] == "1":
                solution = 2**f + solution
                f = f-1
            else:
                solution = 0 + solution
                f = f-1
        decimal_insert.insert(0,solution)





 #----------------------------------------
    def reset():
        binary_entry.delete(0, END)
        decimal_insert.delete(0, END)


    #------------------------- Text
    B_To_D = Label(binary,text="""BINARY
    TO
    DECIMAL""",font=('Corbel',34),bg='white')
    B_To_D.place(x=40,y=0)

    BINARY = Label(binary,text="THE BAYNRY NUMBER",font=('Corbel',9),bg='white')
    BINARY.place(x=50,y=200)

    DECIMAL = Label(binary,text="THE DECIMAL NUMBER",font=('Corbel',9),bg='white')
    DECIMAL.place(x=50,y=320)


    binary_entry = Entry(binary,font=('Corbel',10),bg='red')
    binary_entry.place(x=50,y=230)


    CONVERTE = Button(binary, text="convert",command=Binary_Full)
    CONVERTE.place(x=50,y=270)


    decimal_insert = Entry(binary,font=('Corbel',10),bg='red')
    decimal_insert.place(x=50,y=350)

    QUIT = Button(binary, text="Quit",command=binary.destroy)
    QUIT.place(x=50,y=400)

    reset = Button(binary, text="Reset",command=reset)
    reset.place(x=100,y=400)



    #-------------------------------




    binary.mainloop
