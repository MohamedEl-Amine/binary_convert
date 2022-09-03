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
    print(L)

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
        print(f)
        
    print(L,',',F)
#----------------------------------------

z= float(input())

if z%1 == 0:
    bin_real(z)
else:
    bin_unreal(z)
