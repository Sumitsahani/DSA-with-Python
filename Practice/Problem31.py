# Upper Lower Equation

# • You are given a string stored in a variable with the name string, containing a mix of upper case and lower case English character S
# • The length of the string is stored in stored in a variable with the n ame N
# • You have to solve the equation 7*y + 2*x, where x is the numbe r of small-case English characters in the string,
# while y is the number of upper-case English characters in the string
# For example, consider the value stored in N = 5, and string = AmanZ
# • The number of upper case characters in the string is 2-A, Z, an d the number of small case characters in the string is 3m, a, n
# • Therefore, the value of the equation 7*y + 2*x, becomes 7*2 + 2*3 = 20, which is the required answer


def UpperLower(strings):
    Upper=0
    lower=0
    for i in strings:
        if i.isupper():
            Upper+=1
        elif i.islower():
            lower+=1
    print(7*Upper+2*lower)

strings="AmanZ"
UpperLower(strings)