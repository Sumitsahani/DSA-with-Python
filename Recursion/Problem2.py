def num(n):
    if n == 0:
        return
    else:
        num(n - 1)
        print(n)

num(5)

print("-----------------------------------------------------")

def num(n):
    if n == 0:
        return
    else:
        print(n)
        num(n - 1)

num(5)
