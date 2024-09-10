# Problem Statement: Given an integer N return the reverse of the given number.

#-------------------------------------- Brute Force Approach-----------------------------------------#

def revNum(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

num =54321
print(revNum(num))


