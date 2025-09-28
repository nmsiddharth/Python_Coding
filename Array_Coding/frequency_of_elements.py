from collections import Counter

nums = [1,2,3,3,4,5,5,6,6,6,7]

counts = Counter(nums)
print(dict(counts))

#OR

def frequency(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)

#frequency(nums)