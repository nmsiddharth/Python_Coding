rows = 5
for i in range(1,5):
    for k in range(rows-i,0,-1):
        print("  ",end="")
    for j in range(i):
        print("# ",end="")
    print()