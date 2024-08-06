num = [4,3,2,5,6,9,7]

def second_smallest(num):
    first_min= num[0]
    for i in num:
        if i < first_min:
            first_min = i

    second_min = num[0]

    for i in num:
        if i<second_min and i>first_min:
            second_min = i
    print(second_min)

second_smallest(num)
