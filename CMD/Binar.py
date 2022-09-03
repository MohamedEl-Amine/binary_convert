import BinarTK
def Binar_N():
    global number
    number = BinarTK.number
    solution = 0
    for i in range(0,number):
        if binar[i] == "1":
            solution = 2**i + solution   
        else:
            solution = 0 + solution
    decimal_insert.insert(0,solution)

def Binar_R():
    global number
    number = BinarTK.number
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








#for d in range(number):
    #if binar[d] == ".":
        
        
        












