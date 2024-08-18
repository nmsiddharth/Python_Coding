nums = [1,2,3,3,4,5,5,6,6,6,7]

def repeating(nums):
    freq = {}
    for i in nums:
       if i in freq:
           freq[i]+=1
       else:
            freq[i]=1

       if freq[i] == 2:
        print(i)
repeating(nums)