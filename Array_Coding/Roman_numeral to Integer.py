
def romanToInt(s):
    rom_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    output = 0
    n = len(s)

    for i in range(n):
        # check if there is a next character
        if i < n-1 and  rom_dict[s[i]] < rom_dict[s[i+1]]:
            output -= rom_dict[s[i]]
        else:
            output += rom_dict[s[i]]

    return output
print(romanToInt('IV'))



# 1. Form a dict
# 2. Loop through string using range()
# 3. check if i < n-1 (if there is nxt char) current value < nxt value ---> subtract current value from output
# 4. else -----> Add current value to output