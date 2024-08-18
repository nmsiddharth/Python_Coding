#(a positive integer that is equal to the sum of its proper divisors)

num = int(input("Enter Number"))
temp = num
def proper_divisors(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum = sum+i

    if temp==sum:
        print("perfect")
    else:
        print("Not perfect")

proper_divisors(num)
