num = int(input("Enter number"))

def fibonacci(num):
    first = 0
    second = 1
    third = 0

    for i in range(2,num+1):
        third = first +second
        first = second
        second = third
    print(third)

fibonacci(num)