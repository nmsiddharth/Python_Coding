# pivot index is index where left_sum == right_sum wrt to that index

nums = [1, 7, 3, 6, 5, 6]

def check(nums):
    total = sum(nums)
    left_sum = 0
    
    for i,x in enumerate(nums):
        right_sum = total - left_sum - x
        
        if left_sum==right_sum:
            print(i)
        
        left_sum+=x  
check(nums)        