
# An Armstrong number is a number that is equal to the sum of its own digits raised to the power of
# the number of digits.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

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