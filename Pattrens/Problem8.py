# Pattern - 8: Inverted Star Pyramid

def starPyramid(num):
    for i in range(0,num):
        for k in range(0,i):
            print(" ", end=" ")
        for j in range(1, 2*(num-i)):
            print("*" ,end=" ")
        print()

starPyramid(5)