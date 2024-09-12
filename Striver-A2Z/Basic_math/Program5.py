# Print all Divisors of a given Number

def DivNum(num):
    arr = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i)
    print(arr)

num = 36
DivNum(num)