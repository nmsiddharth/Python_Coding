str = "Crist123i3an43o"

def rem_non_char(str):
    new = []
    for i in str:
       if i.isalpha():    # checks if character is alphabet or not
           new.append(i)

       s = "".join(new)
    print(s)
rem_non_char(str)