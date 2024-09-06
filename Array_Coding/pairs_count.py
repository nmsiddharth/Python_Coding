arr = [1,2,1,3,1,2,2]

def check(arr):
    count = 0
    output = {}

    for i in arr:
        if i in output:
            output[i]+=1
            if output[i] % 2 == 0:
                count+=1

        else:
            output[i]=1
    print(f"Pairs : {count}")


check(arr)