# Pattern - 7: Star Pyramid

def starPyramid(num):
    for i in range(0,num):
        for k in range(0,num-i-1):
            print(" " ,end="")
        for j in range(1,2*(i+1)):
            print("*", end="")
        print()
starPyramid(5)