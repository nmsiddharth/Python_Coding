arr1 = [15, 14,91,9, 1]
arr2 = [24, 5, 21, 85 ]
def disjoint(arr1,arr2):
    flag = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                flag = 1

    if flag == 0:
        print("Arrays are disjoint")
    else:
        print("Not disjoint")

    # OR

''' set1 = set(arr1)
    set2 = set(arr2)

    if set1.isdisjoint(set2):
        print("Arrays are disjoint")
    else:
        print("Not disjoint") '''

disjoint(arr1,arr2)