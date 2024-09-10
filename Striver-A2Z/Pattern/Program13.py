def triangle(n):
    for i in range(0,n+1):
        for j in range(1,i):
            print(j,end=" ")
        print()
n=5
triangle(n)