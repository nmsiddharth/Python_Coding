arr = [16,4,23,8,15,42,1,2]
target = 19
def two_sum(arr,target):
    num_arr = {}        # key = arr values and value = index  , works as HashTable
    for i in range(len(arr)):
        comp = target - arr[i]

        if comp in num_arr:
            return [num_arr[comp],i]   # returns value of comp key and index of current array element

        num_arr[arr[i]] = i   # If comp not in num_arr, assign current value to num_arr[arr[i]] (current element) and i as its value. In this way we can later find comp using this arr[i].

    return None

result = two_sum(arr,target)

if result is not None:
    print(f"{result[0]},{result[1]}")
else:
    print("Not found")



