# Pattern-1: Rectangular Star Pattern

def Rectangular(num):
    for i in range(0, num,1):
        for j in range(0,num,1):
            print("*",end=" ")
        print()

Rectangular(5)