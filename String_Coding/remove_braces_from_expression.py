def check(str):
    s= str.maketrans("","","[]{}()")
    str = str.translate(s)
    print(str)

str = "a-(b+c)"
check(str)