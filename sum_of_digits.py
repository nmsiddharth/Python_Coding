num = int(input("Enter Number"))

def check(num):
    count = 0
    while num>0:
        rem = num%10
        count = count+rem
        num = num//10

    print(count)
check(num)
