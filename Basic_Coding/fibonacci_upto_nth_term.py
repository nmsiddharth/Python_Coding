num = int(input("Enter number till u need fibonacci series"))

def fibonacci(num):
    first = 0
    second = 1
    third = 0
    print(first)
    print(second)

    for i in range(2,num+1):
        third = first + second
        first = second
        second = third
        print(third)

fibonacci(num)