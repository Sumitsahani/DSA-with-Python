def halfDiamond(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()
    for i in range(n-1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

n = 5
halfDiamond(n)