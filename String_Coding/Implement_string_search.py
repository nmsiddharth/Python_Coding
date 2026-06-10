
                        # just like using str.find() or str.index()
haystack = 'hello'
needle = 'll'

def check(haystack,needle):
    
    L = len(haystack)
    N = len(needle)
    
    for  i in range(L-N+1):
        if haystack[i:i+N]==needle:
            return i
    
    return -1

print(check(haystack,needle))    