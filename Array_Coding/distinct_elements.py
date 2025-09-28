nums = [1,2,3,3,4,5,5,6,6,6,7]

def distinct(nums):
    freq = {}
    lt = []
    for i in nums:
       if i not in freq:
           freq[i]=1
           print(i)
           lt.append(i)
    print(lt)
    
distinct(nums)