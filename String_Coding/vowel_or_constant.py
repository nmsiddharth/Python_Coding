

class vowel_constant:
    def __init__(self,char):
        self.char = char.lower()
    def check(self):
        if self.char in 'aeiou':
            print(f"{self.char} is vowel")
        else:
            print(f"{self.char} is consonant")

obj = vowel_constant('f')
obj.check()
