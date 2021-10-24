'''
Graphs in Python:
1. DFS with recursion -- stacks 
2. BFS with iteration -- queue and stacks 

*** Problem Description *** 
We have a bunch of airports (nodes/vertices) with their connections (edges)
From an airport, we can reach different airports, hence creating a connected 
and directed graph.

To store the graph, we can use a structure like adjacency list. 
i.e., our graph looks like:
A: [B, C, D]
B: [A, D]
C: [B, D]

A few problems (4) that we need to solve includes:
1. Simply print all airpots in the graph  
2. Given a start and end:
    a. print all possbile paths from start to end 
    b. print the shortest path from start to end 
    c. return whether it is possible (True/False) to reach an end from a start 
'''

    ###########################################################################

from typing import TextIO


class AirMap:
    def __init__(self):
        self.airports = {}

    def showGraph(self):
        print(self.airports)

    def construct_Graph(self, start, end):
        if start not in self.airports:
            self.airports[start] = [end]
        else:
            self.airports[start].append(end)

    ###########################################################################

    ######  RETURN ALL NODES or VERTICES --- BFS  ######

    # We need to have a start node --> from where we will print all possible nodes 
    # It is good to use BFS for simply printing all nodes 

    # ALL VERTICES/NODES (not edges) --> for edges, we use DFS 
    def print_all_Airports_BFS(self, start):
        # BFS Way 
        # Visited = []
        # toVisit = [start] -- acts like a queue (FIFO) 
        # we pop from toVisit, and get its neighbors -- currNode
        # popped node or currNode goes into visited
        # push all neighbors of currNode into toVisit 
        # repeate till we have nodes toVisit 

        visited = []
        toVisit = [start]

        while toVisit:
            currNode = toVisit.pop(0) # acts like queue -- pop(0) because we append below *L2
            
            if currNode not in visited:      # we don't want to insert currNode again 
                visited.append(currNode)

                if currNode in self.airports:
                    for neighbors in self.airports[currNode]:
                        if neighbors not in toVisit:
                            toVisit.append(neighbors) # *L2 

        return visited



    ###########################################################################

    ### Note the difference between DFS vs BFS 
    ### If finding paths/edges     -->  DFS             
    ### If finding nodes/vertices  -->  BFS      -->    If finding shortest path, we can use BFS 

    ###########################################################################
    


    ###### ALL POSSIBLE PATHS --- BFS  ######

    # From a start --> end (All possible paths)
    # paths are not vertices, they are edges --> We should use DFS 
    # i.e., A-B-D, A-D, A-C-D, A-C-B-D 
    
    # start acts as the current node in the iteration -- and we recursively change it (e.g., like a root)
    # Visited = we keep track of the nodes that we have already visited --> toVisit in BFS  
    # Paths =  the paths that we have visited so far --> visited in BFS 
    def DFS_Helper(self, start, end, visited, paths):
        visited[start] = True 
        paths.append(start)

        # Base condition -- our recursion stops when we hit the endPoint 
        if start == end:
            # How we can manipulate this part to return something 
            print(paths)
        else:   
            # We recursively go to the neighbor of each 
            for neighbor in self.airports[start]:

                # The reason for this part is --> since we don't have "D" as the key in the Graph
                if neighbor == end:
                    paths.append(end)
                    print(paths)
                    paths.pop()
                    break
                if visited[neighbor] == False:
                    self.DFS_Helper(neighbor, end, visited, paths)

        # We need to pop from the Paths in two cases:
        # 1. If we hit the endPoint --> start == end 
        # 2. We visited all the neighbor nodes of a key -- recursion stops -- we pop the last node                 

        paths.pop()
        visited[start] = False        

    
    def all_Possible_Paths_DFS(self, start, end):
        
        # We use this paths to store our paths in the current recursion and update this overall for multiple paths
        paths = []
        
        # We use this dictionary to store all the vertices/nodes of the graph to keep track of the visited nodes 
        # i.e., {A:False, B:False, C:True}  
        # Key = Vertex(node), Value = True/False         
        visited = {v:False for v,_ in self.airports.items()}
        # 


        self.DFS_Helper(start, end, visited, paths)
    
    ###########################################################################
                # NEW SESSION BELOW # IGNORE ABOVE #
    ###########################################################################





    # Is it possible to reach an end from a start? 
    def is_Possible_Path(self, start, end):
        pass 


    def allNodes_BFS(self, start):
        visited = []
        toVisit = [start]
        visited.append(start)
        while toVisit: 
            currNode = toVisit.pop(0) # A 
            
            if currNode in self.airports:
                for neighbor in self.airports[currNode]: 
                    if neighbor not in visited:
                        visited.append(neighbor) 
                        toVisit.append(neighbor)    
        return visited


    def allNodes_DFSHelper(self, start, paths):

        if start not in paths:
            paths.append(start)

        for neighbor in self.airports[start]:
            if neighbor in self.airports:
                if neighbor not in paths:
                   self.allNodes_DFSHelper(neighbor, paths)
            else:
                # if we have a node that is not a key --> since it has no neighbors
                paths.append(neighbor)


    def allNodes_DFS(self, start):
        paths = []
        self.allNodes_DFSHelper(start, paths)        
        return paths 


    def findShortestPath_BFS(self, start, end):
        pass 




    
    def findAllPaths_DFSHelper(self, start, end, toVisit, visited):
        toVisit[start] = True 
        visited.append(start)

        if start == end:
            print(visited)

        else:
            if start in self.airports:
                for neighbor in self.airports[start]:
                    if neighbor in toVisit:
                        if toVisit[neighbor] == False:
                            self.findAllPaths_DFSHelper(neighbor, end, toVisit, visited)
                    else:
                        visited.append(neighbor)
                        print(visited)
                        visited.pop()

        toVisit[start] = False
        visited.pop()



    def findAllPaths_DFS(self, start, end):
        visited = [] # We store the paths here 
        toVisit = {key:False for key in self.airports.keys()}

        self.findAllPaths_DFSHelper(start, end, toVisit, visited)        




###########################################################################

# Main Function 
air = AirMap()
air.construct_Graph("A", "B")
air.construct_Graph("A", "C")
# air.construct_Graph("A", "D")

air.construct_Graph("B", "A")
air.construct_Graph("B", "D")

air.construct_Graph("C", "B")
# air.construct_Graph("C", "D")

# air.showGraph()

#### Start Time:    9:00 PM 

# Task 1: Print all nodes in the graph 
# This task --> can be done with both DFS and BFS --> However, BFS is preferred 

print("Print All Nodes with DFS:    ", air.allNodes_DFS("A"))
print("Print All Nodes with BFS:    ", air.allNodes_BFS("A"))


# Task 2: Get all paths in the graphs 
# This is done via DFS 
print("Print All paths from A to D: ")
air.findAllPaths_DFS("A", "D")




# Task 3: Get the shortest path 
# This is done via BFS 


# Task 4: Return if a path is posssible between 2 nodes 
# This is done via DFS 
# air.is_Possible_Path("A", "C")

# Task 5: Detect if there are any cycles in the graph  
# This is done via DFS 












###########################################################################

# startPoint = "A"
# print("\n*** Print All nodes from the Starting Point", startPoint, "***")
# print(air.print_all_Airports_BFS(startPoint), "\n")

# startPoint = "B"
# print("\n*** Print All nodes from the Starting Point", startPoint, "***")
# print(air.print_all_Airports_BFS(startPoint), "\n")

# startPoint = "C"
# print("\n*** Print All nodes from the Starting Point", startPoint, "***")
# print(air.print_all_Airports_BFS(startPoint), "\n")

###########################################################################


# print("\n<><><><><><><><><><><><><><>\n")

# startPoint = "C" 
# endPoint = "D"
# print("\n*** Print All **PATHS** from the Starting Point", startPoint, "***")
# air.all_Possible_Paths_DFS(startPoint, endPoint)


###########################################################################




















