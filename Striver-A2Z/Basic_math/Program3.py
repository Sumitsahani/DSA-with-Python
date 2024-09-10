# Check if a number is Palindrome or Not

def palindrome(num):
    rev = 0
    temp = num
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev == temp
num=112233
print(palindrome(num))

