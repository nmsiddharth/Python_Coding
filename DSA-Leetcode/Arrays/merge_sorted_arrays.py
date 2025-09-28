arr1 = [1,3,5,7]
arr2 = [0,4,6]

merge_arr = []

merge_arr = arr1 + arr2    # Not efficient bcoz we need to merge and sort. O((n+m)log(n+m))
merge_arr.sort()
print(merge_arr)
