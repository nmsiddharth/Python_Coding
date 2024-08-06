nums = [1,2,3,3,4,5,5,6,6,6,7]

def non_repeating(nums):
    freq = {}
    for i in nums:
       if i in freq:
           freq[i]+=1
       else:
            freq[i]=1

    for i in nums:
        if freq[i] == 1:
            print(i)

non_repeating(nums)