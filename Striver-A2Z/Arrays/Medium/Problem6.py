# Stock Buy And Sell
# Example 1:
# Input:
#  prices = [7,1,5,3,6,4]
# Output:
#  5
# Explanation:
#  Buy on day 2 (price = 1) and 
# sell on day 5 (price = 6), profit = 6-1 = 5.

def sellBuy(arr):
    mini = float("inf")
    max_profit = 0
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        elif arr[i] - mini > max_profit:
            max_profit = arr[i] - mini
    return max_profit
arr = [7, 1, 5, 3, 6, 4]
print(sellBuy(arr))


