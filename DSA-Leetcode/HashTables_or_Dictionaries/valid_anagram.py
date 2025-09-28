'''
Anagram is condition where frequencies of 2 strings should be same.
Return TRUE if it is anagram, else return FALSE
'''

from collections import Counter

def check():
    s = "race"
    t = "care"

    return Counter(s) == Counter(t)

print(check())

