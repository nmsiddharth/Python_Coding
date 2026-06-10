input = 'hello world'

def check(input):
    result = []
    upper_nxt_case = True
    
    for char in input:
        if char.isalpha():
            if upper_nxt_case:
                result.append(char.upper())
            else:
                result.append(char.lower())
            
            upper_nxt_case = not upper_nxt_case
        else:
            result.append(char)
            
    result = ''.join(result) 
    print(result)        
            
check(input)                    