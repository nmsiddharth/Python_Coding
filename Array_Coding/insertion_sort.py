arr = [40,30,20,10]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key     # it means that j is -1, so it has come out of while loop
    print(arr)  

insertion_sort(arr)