# Pattern-5: Inverted Right Pyramid

def inverted(num):
    for i in range(0, num+1):
        for j in range(num,i,-1):
            print("*", end=" ")
        print()
inverted(5)