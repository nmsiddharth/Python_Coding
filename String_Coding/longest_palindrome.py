from collections import Counter

str = "abccccdd"

def check(str):
    count = Counter(str)
    res = 0
    
    for cnt in count.values():
        if cnt%2==0:
            res+=cnt
    
    for cnt in count.values():
        if cnt%2!=0:
            res+=1
            break
    
    print(res)
    
check(str)                