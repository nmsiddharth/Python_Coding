arr =[10, -20, -30, 0, 70, -80, -20]

def max_product(arr):
    left = 1
    right =1
    result = arr[0]

    for i in range(len(arr)):
        left = left =1 if left == 0 else left
        right = right= 1 if right ==0 else right

        left *= arr[i]
        right *= arr[len(arr)-1-i]

        result = max(result,max(left,right))
    print(result)

max_product(arr)