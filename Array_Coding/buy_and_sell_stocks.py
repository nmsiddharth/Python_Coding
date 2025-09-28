arr= [7, 1, 5, 6, 4]

def buy_sell(arr):
    max_profit = 0
    buy = arr[0]
    for i in range(1,len(arr)):
        if buy>arr[i]:    # To buy lowest stock
            buy = arr[i]   # buy = lowest stock
        elif arr[i]-buy >max_profit:
            max_profit = arr[i] - buy

    print(max_profit)

buy_sell(arr)


# Here, Buy = lowest stock value(1)
#       Sell = Highest stock value(6)
# 7 is not considered bcoz it comes before value 1 [ value that comes beofre 1 is not considered]. That's y sort() is not used in this problem