'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

nums = [100,4,200,1,3,2]

def check(nums):
    longest = 0
    hm = {}
    
    for num in nums:
        hm[num] = False
        
    for num in nums:
        current_length = 1
        
        next = num+1
        while next in hm and not hm[next]:
            current_length+=1
            hm[next] = True
            next+=1
        
        prev = num-1
        while prev in hm and not hm[prev]:
            current_length+=1
            hm[prev] = True
            prev-=1
        
        longest = max(longest,current_length)
    
    return longest


print(check(nums))            