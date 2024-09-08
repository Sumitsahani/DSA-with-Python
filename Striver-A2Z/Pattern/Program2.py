def triangle(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print("*",end=" ")
        print()
n=5
triangle(n)