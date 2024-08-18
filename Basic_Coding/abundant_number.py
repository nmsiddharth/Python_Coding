# If the sum of all its proper divisors, denoted by sum(n), is greater than the number's value)

num = int(input("Enter Number"))
temp = num

def proper_divisors(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum = sum+i

    if temp<sum:
        print("Abundant")
    else:
        print("Not Abundant")

proper_divisors(num)