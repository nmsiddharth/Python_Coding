strrr= "Cristiano"
str = strrr.lower()
def check(str):
    new = []
    for i in str:
        if i not in 'aeiou':
            new.append(i)
        s = "".join(new)
    print(s)

check(str)