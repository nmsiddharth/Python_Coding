num = int(input("Enter Number"))
temp = num
length = len(str(num))
def armstrong(num):
    sum =0
    while num>0:
        rem = num%10
        sum = sum+rem**length
        num=num//10
    print(sum)

    if sum==temp:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong(num)