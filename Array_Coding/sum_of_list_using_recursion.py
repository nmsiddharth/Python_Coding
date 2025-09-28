# lst = [1,2,3,4]
# n = len(lst)
# def check(lst,n):
#     sum = 0
#     if n==0:
#         return n
#     else:
#         sum+=lst[n-1]
#         return check(lst,n-1)

# print(check(lst,n))

lst = [1, 2, 3, 4]

def sum_recursive(lst, n):
    # Base case: if n is 0, the sum is 0
    if n == 0:
        return 0
    # Recursive step: add the current element and call the function for the rest of the list
    else:
        return lst[n - 1] + sum_recursive(lst, n - 1)

# The variable 'n' should be the length of the list to sum all elements
n = len(lst)
print(sum_recursive(lst, n))