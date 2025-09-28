num1 = 4
num2 =12

def check(num1,num2):
    gcd = 1
    for i in range(1,min(num1,num2)+1):

        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    print(gcd)

check(num1, num2)

# OR
# Using Euclid's Algorithm
def example(num1,num2):
    while num2!=0:
        num1,num2 = num2,num1%num2
    return num1

#print(example(num1,num2))






















































