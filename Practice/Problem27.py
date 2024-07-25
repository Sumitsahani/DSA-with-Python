# The Eligibility Checker
# Description
# You are designing a program for a voting eligibility checker. To be eligible to vote, a person must be at least 18 years old and should not have any criminal records. Write a program that checks a person's age and criminal record to determine their eligibility to vote.
# Write a program to determine if a person is eligible to vote.
# Input
# Two lines of input:
# 1. An integer 'age' (1 <= age <= 120), representing the person's age.
# 2. A boolean 'has Criminal Record', indicating whether the person has a criminal record (True or False).
# A message indicating whether the person is eligible to vote or not. If eligible, print "Eligible to Vote"; otherwise, print "Not Eligible to Vote."

# Hint
# In the sample Input, the age is22which is greater than 18, andfalseindicates that the person does not have any criminal records. Hence, the output is "Eligible to Vote".



def EligibilityCheck(age):
    if age>=18:
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

age=int(input())
EligibilityCheck(age)

