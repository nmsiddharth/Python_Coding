num = int(input("Enter number"))

def fact(num):

    for i in range(1,num+1):
        if num%i==0:
            print(i)

fact(num)