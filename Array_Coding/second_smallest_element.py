
num = [4,3,2,5,6,9,7]

def second_smallest(num):

    smallest = min(num[0],num[1])
    second_smallest = max(num[0],num[1])

    for i in range(2,len(num)):
        if num[i]<smallest:
            second_smallest = smallest
            smallest = num[i]
        elif num[i]<second_smallest and num[i]!=smallest:
            second_smallest = num[i]

    print(second_smallest)

second_smallest(num)
