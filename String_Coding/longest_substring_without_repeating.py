
def check(str):
    max_len = 0
    i = 0
    j = 0
    l = len(str)
    c_set = set()
    while i<l and j<l:
        if str[j] not in c_set:
            c_set.add(str[j])
            j+=1
            max_len = max(max_len,j-i)
        else:
            c_set.remove(str[i])
            i+=1

    print(max_len)

str = "aacbbccc"
check(str)