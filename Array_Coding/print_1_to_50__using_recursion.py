n = 50

def check(n):

    if n==0:
        return

    #check(n-1)  # ascending
    print(n)
    check(n-1)   # descending

check(n)