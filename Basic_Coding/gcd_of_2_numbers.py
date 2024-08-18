num1 = 4
num2 =12

def check(num1,num2):

    for i in range(1,min(num1,num2)+1):
        gcd = 1
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    print(gcd)


check(num1, num2)























































