num = 1111

def check(num):
    decimal = 0
    i = 0
    while num>0:
        rem = num%10
        decimal+=rem*(2**i)
        num = num//10
        i+=1

    print(decimal)

check(num)



