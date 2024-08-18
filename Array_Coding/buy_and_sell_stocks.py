arr= [7, 1, 5, 6, 4]

def buy_sell(arr):
    max_profit = 0
    buy = arr[0]
    for i in range(1,len(arr)):
        if buy>arr[i]:
            buy = arr[i]
        elif arr[i]-buy >max_profit:
            max_profit = arr[i] - buy

    print(max_profit)

buy_sell(arr)
