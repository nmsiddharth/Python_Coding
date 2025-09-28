def compress_str(s):
    new_s = " "
    count = 1

    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            new_s+= str(count)+ s[i-1]
            count=1    # reset the counter
    #To handle last char
    new_s+= str(count)+s[-1]
    print(new_s)

s = "aabbbbccdeeeffffgg"
compress_str(s)