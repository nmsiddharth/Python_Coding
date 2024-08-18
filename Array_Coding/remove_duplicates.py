nums = [1,2,3,3,4,5,5,6,6,6,7]

# Same as Distinct elements program
def rem_duplicates(nums):
#    freq = {}
#    unique = []
#    for i in nums:
#       if i not in freq:
#           freq[i]=1
#           unique.append(i)
#    print(unique)

        # OR

    print(list(set(nums)))

rem_duplicates(nums)