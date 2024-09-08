def inverted_pyramid(num):
    for i in range(num, 0, -1):
        for j in range(num, i, -1):
            print(" ", end=" ")
        for k in range(0, 2*i-1):
            print("*", end=" ")
        print()

num = 5
inverted_pyramid(num)