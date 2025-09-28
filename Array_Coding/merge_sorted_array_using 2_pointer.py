arr1 = [1,2]
arr2 = [3,4]

def check(arr1,arr2):
    
    merge_arr = []
    p1 = 0
    p2 = 0


    if len(arr1)==0:
        merge_arr = arr2
    
    if len(arr2)==0:
        merge_arr =arr1
            
    while p1 < len(arr1) and p2 <len(arr2):
        if arr1[p1] < arr2[p2]:
            merge_arr.append(arr1[p1])
            p1+=1
        else:
            merge_arr.append(arr2[p2])
            p2+=1
            
        # These 2 while loops are for handling inputs when there different length of inputs in arr1 and arr2. Once one of the arrays is exhausted (i.e., p1 reaches len(arr1) or p2 reaches len(arr2)), above main loop terminates.
    while p1<len(arr1):
        merge_arr.append(arr1[p1])
        p1+=1
                
    while p2<len(arr2):
        merge_arr.append(arr2[p2])
        p2+=1            
    
    # To find median of merge_arr
    n = len(merge_arr)
    if n%2==1:
        middle_index = n//2
        return merge_arr[middle_index]       
    else:
        middle_index1 = n//2 - 1
        middle_index2 = n//2  
        return (merge_arr[middle_index1] + merge_arr[middle_index2]) /2
        
    #print(merge_arr)        
out = print(check([1,3],[2]))  #    ------> 2
res = print(check([1,2],[3,4])) #   ------> 2.5