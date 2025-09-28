
# class anagram:
#     def __init__(self,str1,str2):
#         self.str1 = str1.lower()
#         self.str2 = str2.lower()

#     def check(self):
#         if sorted(self.str1) == sorted(self.str2):
#             print("anagram")
#         else:
#             print("Not anagram")

# obj = anagram("care","race")
# obj.check()

from collections import Counter

s1 = "care"
s2 = 'race'
def check(s1,s2):
    if Counter(s1)==Counter(s2):
        return True
    else:
        return False

if check(s1,s2):
    print("Anagram")
else:
    print("Not Anagram")       
