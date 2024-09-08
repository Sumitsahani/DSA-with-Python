# Tom and Jerry are playing a game of cards. They play N rounds, and they keep the scores of all the rounds in the form of an array. If Tom wins a particular round, the value at that particular index is updated to 1, and if Jerry wins that particular round, the value at that index is updated to 0.
# You are given an array of size N, denoting the winners in the various rounds. If Tom wins more rounds than Jerry, then print "Tom", else if Jerry wins more rounds than Tom, print "J erry", else print "Another round".
# Input
# The first line of the input contains N, the number of rounds Tom & Jerry played.
# Next line contains N space separated integers contains 1's and 0's, where 1 indicates that Tom won that round, and 0 indicates that Jerry won that round.
# Constraints
# 1 <= N <= 100
# 0 <= A[i] <= 1
# Output
# If Tom wins more rounds than Jerry, print "Tom", else if Jerry wins more round than Tom, print "Jerry", else print "Another round".


def TomJerry(arr):
    countTom=0
    countJerry=0
    for i in arr:
        if i==1:
            countTom+=1
        else:
            countJerry+=1
    if countTom>countJerry:
        print("Tom")
    elif countJerry>countTom:
        print("Jerry")
    else:
        print("Another Round")

arr=[1,1,1,0,0,0,0]
TomJerry(arr)