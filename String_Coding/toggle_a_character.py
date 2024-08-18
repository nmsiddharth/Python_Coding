str = "SiDDhartH"

def check(str):
    new = ""
    for i in str:
        if i.isupper():
            new+= i.lower()
        elif i.islower():
            new+= i.upper()
    print(new)

check(str)