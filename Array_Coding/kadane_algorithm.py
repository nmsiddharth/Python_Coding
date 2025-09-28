
#  maximum subarray problem

#arr = [-2,-3,4,-1,-2,1,5,-3]
arr =  [-5, -2, -8]
# def kadane(arr):
#     sum = arr[0]
#     max_sum = arr[0]

#     for i in range(1,len(arr)):
#         if sum>=0:
#             sum+=arr[i]
#         else:
#             sum = arr[i]

#         if sum>max_sum:
#             max_sum = sum
#     print(max_sum)

# kadane(arr)

def kadane(arr):
    curr = arr[0]
    max_sum = arr[0]

    for i in range(1,len(arr)):
        curr = max(arr[i],curr+arr[i])
        max_sum = max(max_sum,curr)
    print(max_sum)

kadane(arr)