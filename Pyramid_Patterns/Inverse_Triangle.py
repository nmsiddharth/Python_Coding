rows = 6

for i in range(1,rows):
    for k in range(i):
        print(" ",end="")
    for j in range(rows,i,-1):  # or for j in range(rows-i,0,-1):
        print("# ",end="")
    print()
    
    
    # ******
    #  *****
    #   ****
    #    ***
    #     **
    #      *