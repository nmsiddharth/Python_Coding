l = [1, [2, [3, 4]], 5]

def check(l):
    flat_list = []
    for i in l:
        if isinstance(i,list):
            flat_list.extend(check(i))
        else:
            flat_list.append(i)
    return flat_list

print(check(l))                