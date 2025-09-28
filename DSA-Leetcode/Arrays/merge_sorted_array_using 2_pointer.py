arr1 = [1,3,5,7]
arr2 = []

def check(arr1,arr2):
    
    merge_arr = []
    p1 = 0                              # Which is smaller , add to list and increment and again compare
    p2 = 0


    if len(arr1)==0:
        merge_arr = arr2
    
    if len(arr2)==0:
        merge_arr ==arr1
            
    while p1 < len(arr1) and p2 <len(arr2):
        if arr1[p1] < arr2[p2]:
            merge_arr.append(arr1[p1])
            p1+=1
        else:
            merge_arr.append(arr2[p2])
            p2+=1
            
    while p1<len(arr1):
        merge_arr.append(arr1[p1])
        p1+=1
                
    while p2<len(arr2):
        merge_arr.append(arr2[p2])
        p2+=1            
            
    print(merge_arr)        
check(arr1,arr2)