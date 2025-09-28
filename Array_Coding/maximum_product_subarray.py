arr =[10, -20, -30, 0, 70, -80, -20]

# def max_product(arr):
#     left = 1
#     right =1
#     result = arr[0]

#     for i in range(len(arr)):
#         left = left =1 if left == 0 else left
#         right = right= 1 if right ==0 else right

#         left *= arr[i]
#         right *= arr[len(arr)-1-i]

#         result = max(result,max(left,right))
#     print(result)

# max_product(arr)

def max_product(arr):
    res = arr[0]
    max_p  = 1
    min_p = 1
    
    for n in arr:            
        if n == 0:
            max_p = 1
            min_p = 1
            continue
        
        temp_max = max(n, max_p*n, min_p*n)    # temp_max is used bcoz, if max_p was used instead of temp_max , for min_p : max_p would be updated max_p
        min_p = min(n, max_p*n, min_p*n)
        max_p = temp_max

        res = max(res,max_p)
    print(res)     
    
max_product(arr)