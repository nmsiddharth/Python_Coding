arr = [1,2,3,4,5]
k = 3
def circular_rotation(arr,k):
    j = 1
    while j<=k: 
        temp = arr[len(arr) - 1]     # store last element in temp 
        for i in range(len(arr)-1,0,-1):      
            arr[i] = arr[i-1]          # move each element to right side

        arr[0] = temp     # put first element with temp  
        j+=1
    print(arr)

circular_rotation(arr,k)
