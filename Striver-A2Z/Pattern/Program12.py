def dualTriangle(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if j <= i:
                print(j, end="")
            else:
                print(" ", end="")
        for j in range(num, 0, -1):
            if j <= i:
                print(j, end="")
            else:
                print(" ", end="")
        print()
num = 4
dualTriangle(num)
