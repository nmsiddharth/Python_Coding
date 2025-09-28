arr = [16,4,23,8,15,42,1,2]
target = 19

def check(arr,target):
    sett = set()
    
    for num in arr:
        comp = target - num
        if comp in sett:
            return True
        
        sett.add(num)
    
    return False    

print(check(arr,target))