# Pattern-2: Right-Angled Triangle Pattern

def rightAngled(num):
    for i in range(0,num+1,1):
        for j in range(0, i):
            print("*", end="")
        print()
rightAngled(5)