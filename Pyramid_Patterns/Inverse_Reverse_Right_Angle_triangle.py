rows = 5

for i in range(1,rows+1):
    for k in range(1,i):
        print("  ",end="")
    for j in range(rows,i-1,-1):
        print("# ",end="")
    print()