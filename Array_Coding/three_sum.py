arr = [-1,0,1,2,-1,-4]
arr.sort()
def three_sum(arr):
    result = set()
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1

        while left<right:
            sum = arr[i]+arr[left]+arr[right]

            if sum==0:
                result.add((arr[i],arr[left],arr[right]))
                left+=1
                right-=1
            elif sum<0:
                left+=1
            else:
                right-=1
    print(result)
three_sum(arr)