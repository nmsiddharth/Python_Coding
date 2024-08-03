# the ratio between the sum of divisors of a number and the number itself.)

num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))

def proper_divisors(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum = sum+i
    return sum

first = proper_divisors(num1)
second = proper_divisors(num2)

if first/num1 == second/num2:
    print("Friendly pair")
else:
    print("Not Friendly pair")