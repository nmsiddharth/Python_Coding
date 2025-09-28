arr = ['a','b','c','d']

# Append
arr.append('e')   # O(1)
print(arr)

# Pop
arr.pop()  # O(1) : Bcoz it removes single(last) element

# Insert
arr.insert(0,'x')  # O(N) : Bcoz we need to shift indices of all N elements , if we want to add new element at begining of array (worst case).

print(arr)
