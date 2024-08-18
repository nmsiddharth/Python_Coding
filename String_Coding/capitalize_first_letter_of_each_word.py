class capitalize:
    def __init__(self,string):
        self.string = string

    def check(self):
        words = self.string.split()
        capitalized_word = [word[0].upper()+word[1:] for word in words if word]
        res = " ".join(capitalized_word)
        print(res)

obj = capitalize("hi iam siddu")
obj.check()
