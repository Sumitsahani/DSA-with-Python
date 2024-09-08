def BinaryTriangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("1" if (i + j) % 2 == 0 else "0", end=" ")
        print()

n = 6
BinaryTriangle(n)
