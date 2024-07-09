# Right-Angled Number Pyramid

def numPyramid(num):
    for i in range(0, num+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

numPyramid(5)