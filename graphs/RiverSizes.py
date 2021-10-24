
########################################################################################################################
############                                    RIVER SIZES                                                 ############ 
########################################################################################################################


# THIS METHOD HAS A DRAWBACK
# We mutate the original matrix -- because we convert 1's to 0's 
# We need to solve this problem with the method of Key:False or something similar without mutating the original array 

def bfs_countRiverSize(matrix, x, y, xlen, ylen):
    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
    Fcounter = 0 
    visited = []
    toVisit = [(x, y)]                  

    while toVisit:
        currNode = toVisit.pop(0) # 
        matrix[currNode[0]][currNode[1]] = 0
        if currNode not in visited:
            visited.append(currNode) # 
            Fcounter += 1

            for neighbor in directions:
                moveTo = (currNode[0] + neighbor[0], currNode[1] + neighbor[1])       # create a tuple of each neighbor

                if moveTo[0] >=0 and moveTo[0] < xlen and moveTo[1] >=0 and moveTo[1] < ylen:   # neighbor should lie within the given boundaries of matrix 
                    if matrix[moveTo[0]][moveTo[1]] == 1:
                        toVisit.append((moveTo[0], moveTo[1]))

    return Fcounter


def riverSizes(matrix):
    nRivers = []
    for i in range(len(matrix)): # 0123
        for j in range(len(matrix[0])): #01234
            if matrix[i][j] == 1:                     # note that i is y-axis while j is x-axis 
                nRivers.append(bfs_countRiverSize(matrix, i, j, len(matrix), len(matrix[0])))
    return nRivers  


# matrix = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
matrix = [[1, 0, 0, 1, 0], 
[1, 0, 1, 0, 0], 
[0, 0, 1, 0, 1], 
[1, 0, 1, 0, 1], 
[1, 0, 1, 1, 0]]
# output should be [4, 1, 2] in any order 

print(riverSizes(matrix))
