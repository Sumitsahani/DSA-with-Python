# Count digits in a number

#-------------------------------------- Brute Force Approach-----------------------------------------#
def countDigit(num):
    count = 0
    while num > 0:
        rem = num % 10
        count += 1
        num = num // 10
    return count

num = 1234
print(countDigit(num))









    

