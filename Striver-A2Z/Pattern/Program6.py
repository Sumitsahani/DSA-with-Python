def pyramid(num):
    for i in range(1, num+1):
        for j in range(num, i, -1):
            print(" ", end=" ")
        for k in range(0, 2*i-1):
            print("*", end=" ")
        print()
num = 5
pyramid(num)
