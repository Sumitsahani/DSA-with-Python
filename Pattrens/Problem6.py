# Pattern - 6: Inverted Numbered Right Pyramid

def numberInverted(num):
     for i in range(num,0,-1):
            for j in range(1,i+1):
                print(j ,end=" ")
            print("")
numberInverted(5)