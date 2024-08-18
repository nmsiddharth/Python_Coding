arr = [-2,-3,4,-1,-2,1,5,-3]
def kadane(arr):
    sum = arr[0]
    max_sum = arr[0]

    for i in range(1,len(arr)):
        if sum>=0:
            sum+=arr[i]
        else:
            sum = arr[i]

        if sum>max_sum:
            max_sum = sum
    print(max_sum)

kadane(arr)