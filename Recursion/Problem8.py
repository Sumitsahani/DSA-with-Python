# Palindrome with recursion


def checkPalindrome(string, i, j):
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    else:
        return checkPalindrome(string, i+1, j-1)

string = "racecare"
if checkPalindrome(string, 0, len(string) - 1):
    print("Its a palindrome")
else:
    print("Its not a palindrome")
