arr = [16,4,23,8,15,42,1,2]
target = 19
def two_sum(arr,target):
    num_arr = {}
    for i, num in enumerate(arr):
        comp = target - arr[i]

        if comp in num_arr:
            return [num_arr[comp],i]

        num_arr[num] = i

    return None

result = two_sum(arr,target)

if result is not None:
    print(f"{result[0]},{result[1]}")
else:
    print("Not found")



