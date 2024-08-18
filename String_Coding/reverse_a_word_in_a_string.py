class Reverse:
    def __init__(self,str):
        self.str = str

    def check(self):
        words = self.str.split()
        rev = words[::-1]
        res = " ".join(rev)
        print(res)

obj = Reverse("Siddu is doing coding")
obj.check()