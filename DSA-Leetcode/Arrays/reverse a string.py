string = "Hi my name is Sid"

def check(string):
    if len(string) <=2 or not string:
        print("That's not good")
        
    # rev_str = string[::-1]
    # print(rev_str)
    
    rev = []
    for i in range(len(string)-1,-1,-1):
        rev.append(string[i])

    print(''.join(rev))   # To convert list into string
check(string)