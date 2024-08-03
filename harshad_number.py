# number which is divisible by the sum of its digits

num = int(input("Enter Number"))
temp = num

def check(num):
    sum = 0
    while num>0:
        rem = num%10
        sum = sum+rem
        num = num//10
    return sum

sumDig = check(num)

if temp%sumDig==0:
    print("Harshad Number")
else:
    print("Not Harshad number")
