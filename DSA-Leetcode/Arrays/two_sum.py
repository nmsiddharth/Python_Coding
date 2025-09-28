nums = [2,7,11,15] 
target = 9

def check(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        
        if comp in hashmap:
            return [hashmap[comp],i]

        hashmap[nums[i]] = i 
        
    return None

print(check(nums,target))       