
##############################################################################################################
##############################################################################################################

# If word is found, return the entire word, else return None
def boggleBoardComplexDFS(board, row, col, word, visited, directions, counter):
    
    isFound = False 
    visited.add((row, col))

    # if the word is not what we are looking for 
    if board[row][col] != word[counter]:
        return False 


    # if we exceed the current word's limit 
    if counter > len(word) - 1:
        return False  


    print(board[row][col], counter, len(word)-1)


    # if we hit the last word + within the counter limits >> we found our word  
    if word[counter] == word[-1] and board[row][col] == word[-1] and counter == len(word) - 1:
        print("REACHED?", board[row][col])
        return True 

    for neighbor in directions:
        
        # check every possible direction/neighbor from the given point 
        moveToX, moveToY = (row + neighbor[0], col + neighbor[1])

        # must stay within the boundaries 
        if moveToX >=0 and moveToX < len(board) and moveToY >= 0 and moveToY < len(board[0]):
            
            # do not recurse on the visited node 
            if (moveToX, moveToY) not in visited:
                isFound = isFound or boggleBoardComplexDFS(board, moveToX, moveToY, word, visited, directions, counter + 1)


    # when backtracking, mark the node as "not visited" 
    visited.remove((row,col))
    return isFound


# Given words --> return all words that belong in the board 
def boggleBoardComplex(board, words):

    # the list of words to return as the final output 
    wordsToReturn = []

    # go to all directions --> vertical, horizantal, diagonal
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1, 1), (1,-1), (-1,1), (-1, -1)] 

    # for each word in the words list -- we look for the first letter in the board and perform a DFS search 
    for word in words:
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = set()
                if board[row][col] == word[0]:
                    WordFoundAt = boggleBoardComplexDFS(board, row, col, word, visited, directions, 0)
                    print(WordFoundAt, word)
                    if WordFoundAt:
                        wordsToReturn.append(word)

    return wordsToReturn



# # # # # # Main Function # # # # # # 

# board = [ ["A", "B", "N", "O"],  ["U", "S", "B", "O"], ["S", "T", "I", "N"] ]

# words = ["HE", "IS", "A", "TOTAL", "AUSTIN", "NOOB", "AND", "BOO"]

# print(boggleBoardComplex(board, words))
# Expected Output:  ["IS", "A", "AUSTIN", "NOOB", "BOO"]








