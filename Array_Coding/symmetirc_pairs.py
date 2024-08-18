arr = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]

def symmetric_pairs(arr):

    print("symmetric pairs are :")

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i][0] == arr[j][1] and arr[j][0] == arr[i][1]:
                print(f"({arr[i][0]},{arr[i][1]})",end=" ")

symmetric_pairs(arr)
