base = int(input("Enter Base"))
power = int(input("Enter power"))

def powerNum(base,power):
    res = 1
    for i in range(1,power+1):
        res*=base
    print(res)
powerNum(base,power)
