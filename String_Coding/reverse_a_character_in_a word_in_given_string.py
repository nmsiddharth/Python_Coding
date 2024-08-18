class Reverse:
    def __init__(self,str):
        self.str = str

    def check(self):
        words = self.str.split()
        rev_char = [word[::-1] for word in words if word]
        res = " ".join(rev_char)
        print(res)

obj = Reverse("Hi Siddu How are u doing")
obj.check()