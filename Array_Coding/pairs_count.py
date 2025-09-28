arr = [1,2,1,3,1,2,2]

def check(arr):
    count = 0
    output = {}

    for i in arr:
        if i in output:
            output[i]+=1
            if output[i] % 2 == 0:    # If key occurs 2 times, value is incremented, so if value is even increase the count
                count+=1

        else:
            output[i]=1
    print(f"Pairs : {count}")
    print(output)

check(arr)