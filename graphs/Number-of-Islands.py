

########################################################################################################################
############                                    NO OF ISLANDS                                               ############
########################################################################################################################


'''
*** Understanding the Problem *** 
    we start from the first element in the grid 
    for every element in the grid:
        We check if the element is 1:
            If yes:
                We set all the neighbor elements which are 1, to 0 (BFS)
                no_of_islands += 1
            If no:
                keep traversing  

    return no_of_islands 


X-axis = len(array[0])  =   Xlen
Y-axis = len(array)     =   Ylen 

every element = (x,y) 

***step 1***
neighbors:
    right   (1,0) 
    left    (-1,0)
    down    (0,1)
    up      (0,-1) 

***step 2***
Boundaries:
    should be between
        0 to Xlen (left to right)
        0 to Ylen (top to bottom)

'''

# Time Complexity:      O(V+E) * no.of.bfs.calls
# Space Complexity:     O(V+E)


def bfs(matrix, x, y, Xlen, Ylen):
    # 4 possible directions -> up, down, left, right 
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    # the node to visit is the starting point 
    queue = [(x,y)]
    
    # while we have nodes to visit 
    while queue:
        currPoint = queue.pop(0)
        matrix[currPoint[0]][currPoint[1]] = "0"
         
        for neighbor in directions:                                                                     # for all 4 neighbors
            currPos = (currPoint[0] + neighbor[0], currPoint[1] + neighbor[1])
             
            if currPos[0] >=0 and currPos[0] < Xlen and currPos[1] >=0 and currPos[1] < Ylen:           # we should be in the boundaries
                if matrix[currPos[0]][currPos[1]] == "1":
                    queue.append((currPos[0], currPos[1]))


def number_of_Islands(matrix):
    nIslands = 0

    # iterate over the matrix  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            # whenever we encounter 1, we apply our DFS 
            if matrix[i][j] == "1":
                bfs(matrix, i, j, len(matrix), len(matrix[0]))
                nIslands+=1 
    return nIslands  

# Main Function 
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(number_of_Islands(grid))

