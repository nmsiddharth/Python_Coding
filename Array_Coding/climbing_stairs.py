# Use fibonacci series

def check(n):
    if n<=2:
        return n
    
    one_step = 1
    two_step = 2
    total = 0
    
    for i in range(3, n+1):
        total = two_step+one_step
        one_step = two_step
        two_step = total
        
    print(total)
    
check(5)        
        
        
        
        