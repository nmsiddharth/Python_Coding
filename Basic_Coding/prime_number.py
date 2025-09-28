num = int(input("Enter Number"))

def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

if prime(num):
    print(num, "is prime number")
else:
    print(num, "is not prime number")

prime(num)