num = [4,3,2,5,6,9,7]

def largest(num):
    max = num[0]
    for i in num:
        if i > max:
            max = i
    print(max)

largest(num)
