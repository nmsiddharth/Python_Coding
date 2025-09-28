s = "itiiindjl"
hashmap = {}

for i in s:
    if i in hashmap:
        hashmap[i] +=1
    else:
        hashmap[i] = 1

max_char = max(hashmap, key = hashmap.get)    # dont use get() --> use only get
print(max_char)            