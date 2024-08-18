rows = 5

for i in range(1,6): 
    for k in range(rows-i,0,-1):
        print(" ",end="")
    for j in range(i):
        print("# ",end="")
    print()

for i in range(1, rows + 1):
    for k in range(i):
        print(" ", end="")
    for j in range(rows-1, i - 1, -1):
         print("# ", end="")
    print()