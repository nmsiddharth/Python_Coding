nums = [1,2,3,5]
# return True if any value appears at least twice in the array, and return false if every element is distinct.

def check(nums):
    hashset = set()
    
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)    # Add element if not present in hashset
    return False    

print(check(nums))