input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

def check(input):
    R = len(input)
    C = len(input[0])
    
    row_set = set()
    col_set = set()
    
    for i in range(R):
        for j in range(C):
            if input[i][j]==0:
                row_set.add(i)
                col_set.add(j)
                
    for i in range(R):
        for j in range(C):
            if i in row_set or j in col_set:
                input[i][j] = 0
    
    print(input)

check(input)                                       