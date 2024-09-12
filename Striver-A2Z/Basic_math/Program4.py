number = 153
k = len(str(number))
sum = 0
temp = number

while temp > 0:
    ld = temp % 10
    sum += ld ** k
    temp //= 10

if sum == number:
    print("An Armstrong number.")
else:
    print(" Not an Armstrong number.")
