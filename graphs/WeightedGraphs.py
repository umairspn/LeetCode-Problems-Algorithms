
# All possible Graph Representations w.r.t. Input
    # Undirected graph -- adjacency list 

# How to implement weighted graphs 
    # Directed weighted 
        # using adjacency
        # using matrix 
    # Undirected weighted
        # using adjacency
        # using matrix 


# Follow Up:    Can we apply both BFS and DFS clearly?              Yes!
# Follow Up:    Can we check if a path exist?                       Yes! 
# Follow Up:    Can we find all possible paths from A to B?         Yes! 
# Follow Up:    Can we find shortest path?  
# Follow Up:    How does Dijkstra comes in?                        
# Follow Up:    How do we detect a cycle? 

# Add WEIGHTS into the structure and perform all above again! 



############################################################# 
# Let's create a graph structure with adjacency List 
    # Directed   --  with and without weights 
    # Undirected --  with and without weights 

# Let's create a graph strucutre with adjacency Matrix 
    # Directed   -- with and without weights 
    # Undirected -- with and without weights 


############################################################
# Undirected + Unweighted 
# Adjacency List Implementation 

class GraphList:
    def __init__(self):
        self.directedGraph = {} 
        self.undirectedGraph = {}

    def populateDirectedGraph(self, routes):
        vertices = set()
        for start, end in routes:
            vertices.add(start)
            vertices.add(end)
            if start not in self.directedGraph:
                self.directedGraph[start] = [end]
            else:
                self.directedGraph[start].append(end) 

        for node in vertices:
            if node not in self.directedGraph:
                self.directedGraph[node] = []

    def printDirectedGraph(self):
        print(self.directedGraph)

    def populateUndirectedGraph(self, routes):
        for start, end in routes:
            if start not in self.undirectedGraph:
                self.undirectedGraph[start] = [end]
            else:
                self.undirectedGraph[start].append(end) 
            
            if end not in self.undirectedGraph:
                self.undirectedGraph[end] = [start]
            else:
                self.undirectedGraph[end].append(start)

    def printUndirectedGraph(self):
        print(self.undirectedGraph)


###### Follow Up: 1  >>  Does a path exist? 

    def isPathExist_DFS(self, start, end, visited, graph): 
        isFound = False 
        visited.add(start) 

        if start == end:
            print("Found path!")
            isFound = True 

        else:
            for neighbor in graph[start]:
                if neighbor not in visited:
                    isFound = isFound or self.isPathExist_DFS(neighbor, end, visited, graph)

        visited.remove(start)
        return isFound


    def isPathExist(self, start, end, isDirected):
        visited = set()

        if isDirected:
            return self.isPathExist_DFS(start, end, visited, self.directedGraph)        
        else:
            return self.isPathExist_DFS(start, end, visited, self.undirectedGraph)        



###### Follow Up: 2  >>  Print all possible paths from A to B 

    def printAllPaths_DFS(self, start, end, visited, paths, graph, finalPaths):
        visited.add(start)
        paths.append(start)

        if start == end:
            # print("found a path:    ", paths)
            finalPaths.append(paths.copy())

        else:
            for neighbor in graph[start]:
                if neighbor not in visited:
                    self.printAllPaths_DFS(neighbor, end, visited, paths, graph, finalPaths)

        visited.remove(start)
        paths.pop()


    def printAllPaths(self, start, end, isDirected):
        visited = set()
        paths = []
        finalPaths = []

        if isDirected:
            self.printAllPaths_DFS(start, end, visited, paths, self.directedGraph, finalPaths)
        else:
            self.printAllPaths_DFS(start, end, visited, paths, self.undirectedGraph, finalPaths)

        return finalPaths


###### Follow Up: 3  >>  Can we detect a cycle in graph 

    def isCycleExist_DFSHelper(self, start, visited, graph, startNode, paths):
        isCycle = False 
        paths.append(start)
        visited.add(start)

        for neighbor in graph[start]:
            if neighbor in visited:
                print("Cycle at ", paths) 
                isCycle = True 
            else:
                if neighbor not in visited:
                    isCycle = isCycle or self.isCycleExist_DFSHelper(neighbor, visited,graph, startNode, paths)

        visited.remove(start)
        paths.pop()
        return isCycle
        

    def isCycleExist(self, start, isDirected):
        
        visited = set()
        paths = []

        if isDirected:
            return self.isCycleExist_DFSHelper(start, visited, self.directedGraph, start, paths)
        else:
            return self.isCycleExist_DFSHelper(start,visited, self.undirectedGraph, start, paths)



# Input Format 
# 1. We are given the routes only 
routes = [["A", "B"], ["A", "D"], ["D", "C"], ["D", "E"], ["B", "C"]]
listGraph = GraphList()

listGraph.populateDirectedGraph(routes)
print("Directed Graph:  ")
listGraph.printDirectedGraph()

listGraph.populateUndirectedGraph(routes)
print("\nUn-directed Graph:  ")
listGraph.printUndirectedGraph()


######## Follow up-1:  Does a path from (start -> end) exist #########

startNode = "D"
endNode = "B"
print("\nDoes A Path Exist between ", startNode, " and ", endNode)

isDirected = True  
print(listGraph.isPathExist(startNode, endNode, isDirected))            # False       

isDirected = False 
print(listGraph.isPathExist(startNode, endNode, isDirected))            # True 



######### Follow up-2: Print all paths from (start -> end) exist #########

startNode = "D"
endNode = "B"


print("\nPrint All Possible Paths between ", startNode, " and ", endNode)
isDirected = True  
print(listGraph.printAllPaths(startNode, endNode, isDirected))

isDirected = False 
print(listGraph.printAllPaths(startNode, endNode, isDirected))



######## Follow up-3: Can we detect a cycle in the graph from a given point #########

startNode = "A"

print("\nDoes a Cycle Exist at ", startNode)

isDirected = True  
print(listGraph.isCycleExist(startNode, isDirected))        # false 

isDirected = False 
print(listGraph.isCycleExist(startNode, isDirected))        # true for all starting points 

