s = " apple % is red#  @in color"

lt = []

for ch in s:
    if ch.isalpha() or ch.isspace():
        lt.append(ch)
        
res = ''.join(lt)
out = " ".join(res.split())    # removes extra space
print(out)        
        
