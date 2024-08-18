arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]


def subset(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    if set2.issubset(set1):
        print(f"{arr2} is subset of {arr1}")
    else:
        print(f"{arr2} is not subset of {arr1}")

subset(arr1,arr2)