num = [1,2,4,5]

def check(num):
    n = len(num)+1
    expected_sum = n*(n+1)//2
    actual_sum = sum(num)
    missing_number = expected_sum - actual_sum
    print(missing_number)
check(num)    