from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

def check(nums, k):
    hashmap = Counter(nums)
    '''
    bcoz dict is unordered , so to maintain order we use bucket. The length is len(nums)+1 bcoz max frequeny of element can be len(nums). 
    So to make sure we start from 1 instead of 0 ,we take 1 extra space for better understanding and make sure to align index and dict values(freq of elements).
    '''
    bucket = [[] for _ in range(len(nums)+1)]   
    
    for key,value in hashmap.items():
        bucket[value].append(key)
        
    result = []
    
    for i in range(len(bucket)-1,0,-1):  # In reverse bcoz , we get top frequent elements
        if bucket[i]:
            for value in bucket[i]:
                if len(result) < k:
                    result.append(value)
                else: 
                    return result    
    return result        

print(check(nums,k))