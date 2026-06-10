arr = [-1,0,1,2,-1,-4]
arr.sort()
def three_sum(arr):
    result = set()
    
    for i in range(len(arr)-2):
        
        if i>0 and arr[i]==arr[i-1]:
            continue
        
        left = i+1
        right = len(arr)-1

        while left<right:
            sum = arr[i]+arr[left]+arr[right]

            if sum==0:
                result.add((arr[i],arr[left],arr[right]))
                left+=1
                right-=1
                
                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1    
                    
            elif sum<0:
                left+=1
            else:
                right-=1
    print(result)
three_sum(arr)



# while left < right:: The inner loop continues as long as the left pointer is less than the right pointer.
# sum = arr[i] + arr[left] + arr[right]: Calculate the sum of the current triplet formed by arr[i], arr[left], and arr[right].
# Case 1: sum == 0 (Triplet Found):
# result.add((arr[i], arr[left], arr[right])): If the sum is equal to zero, we have found a valid triplet. We add it to the result set as a tuple.
# left += 1: Move the left pointer one position to the right.
# right -= 1: Move the right pointer one position to the left.
# Case 2: sum < 0 (Sum Too Small):
# left += 1: If the sum is less than zero, it means we need a larger sum. We move the left pointer one position to the right to consider a larger element.
# Case 3: sum > 0 (Sum Too Large):
# right -= 1: If the sum is greater than zero, it means we need a smaller sum. We move the right pointer one position to the left to consider a smaller element.