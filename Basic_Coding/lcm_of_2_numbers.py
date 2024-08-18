num1 = 2
num2 = 4

def gcd(num1,num2):
    gcd = 1

    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            gcd = i
    return gcd

def check_lcm(num1,num2):
    return num1*num2/gcd(num1,num2)

res = check_lcm(num1,num2)
print(res)