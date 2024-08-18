
class anagram:
    def __init__(self,str1,str2):
        self.str1 = str1.lower()
        self.str2 = str2.lower()

    def check(self):
        if sorted(self.str1) == sorted(self.str2):
            print("anagram")
        else:
            print("Not anagram")

obj = anagram("care","race")
obj.check()
