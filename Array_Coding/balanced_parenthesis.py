str = "([{}])"

def bp(str):
    stack = []
    closeToOpen = {")":"(" , "]":"[" , "}":"{"}

    for char in str:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack

if bp(str):
    print("Balanced")
else:
    print("Not Balanced")