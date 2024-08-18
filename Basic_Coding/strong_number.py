#(sum of factorial of digits is equals to number itself)

num = int(input("Enter Number"))
temp = num
def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact*=i
    return fact

def digits(num):
    sum = 0
    while num>0:
        rem = num%10
        factorialNum = factorial(rem)
        sum = sum+factorialNum
        num = num//10
    print(sum)

    if sum == temp:
        print("Number is Strong Number")
    else:
        print("Number is not Strong Number")
digits(num)




