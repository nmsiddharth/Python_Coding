num = [4,3,2,5,6,9,7]

def smallest(num):
    minimum = num[0]
    for i in num:
        if i < minimum:
            minimum = i
    print(minimum)

smallest(num)
