class First_Non_Repeating:
    def __init__(self,str):
        self.str = str

    def check(self):
        freq = {}
        for i in self.str:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1

        print(freq)

        for j in self.str:
            if freq[j] ==1:
                print(j)
                break

obj = First_Non_Repeating("SiSddu")
obj.check()
