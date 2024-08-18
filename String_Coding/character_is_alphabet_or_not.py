class alphabet:
    def __init__(self,char):
        self.char = char

    def check(self):
        if self.char >='a' and self.char <='z' or self.char>='A' and self.char<='Z' :
            print("Alphabet")
        else:
            print("Not Alphabet")

obj = alphabet('2')
obj.check()

