str = "radar"

# def check(str):
#         if str==str[::-1]:
#             return True
#         return False
# res = check(str)
# if res:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

def check(str):
    i = 0
    j = len(str)-1
    
    while i<j:
        while i<j and not str[i].isalnum():
            i+=1
        while i<j and not str[j].isalnum():
            j-=1
        if str[i].lower()!=str[j].lower():
            return "Not Palindrome"
        i+=1
        j-=1
    return "Palindrome"     

print(check(str))       