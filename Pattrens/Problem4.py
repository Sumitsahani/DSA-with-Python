# Right-Angled Number Pyramid - II

def rightnum(num):
    for i in range(0, num+1):
        for j in range(0,i+1):
            print(i,end="")
        print()
rightnum(5)



