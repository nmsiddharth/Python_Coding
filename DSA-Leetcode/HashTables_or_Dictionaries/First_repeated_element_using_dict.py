arr = [2,5,1,2,3,5,1,2,4]

def check(arr):
    my_dict = {}
    for i in arr:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i] = 1
     
    for j in my_dict:
        if my_dict[j]>=2:
            print(j)
            break

check(arr)                    
