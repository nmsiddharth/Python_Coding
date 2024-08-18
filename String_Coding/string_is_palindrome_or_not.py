str = "rvdar"

def check(str):
        if str==str[::-1]:
            return True
        return False
res = check(str)
if res:
    print("Palindrome")
else:
    print("Not Palindrome")

