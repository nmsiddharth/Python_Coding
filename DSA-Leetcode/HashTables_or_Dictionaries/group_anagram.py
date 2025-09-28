'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def check(strs):
    hashmap = defaultdict(list)
    for s in strs:
        count = [0]*26    # Count = list of 26 zeros
        for char in s:
            count[ord(char) - ord('a')] += 1   # ord() --> conerts letters into ascii value( eg: a --> 97). SO this line created index of these letters and assigns 1 if present.
        hashmap[tuple(count)].append(s)      # count is converted into tuple bcoz key of dictionary cannot be mutuble
    return list(hashmap.values())       

print(check(strs))             