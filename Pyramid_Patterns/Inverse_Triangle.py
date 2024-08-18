rows = 6

for i in range(1,rows):
    for k in range(i):
        print(" ",end="")
    for j in range(rows,i,-1):
        print("# ",end="")
    print()