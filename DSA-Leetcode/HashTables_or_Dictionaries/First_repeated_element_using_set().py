arr = [2,5,1,2,3,5,1,2,4]

def check(arr):
    myset = set()
    
    for i in arr:
        if i in myset:
            print(i)
            break
        myset.add(i)        
check(arr)        