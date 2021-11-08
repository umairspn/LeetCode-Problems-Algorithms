
# All possible Graph Representations w.r.t. Input
    # Undirected graph -- adjacency list 

# How to implement weighted graphs 
    # Directed weighted 
        # using adjacency
        # using matrix 
    # Undirected weighted
        # using adjacency
        # using matrix 


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
        for start, end, weight in routes:
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
        for start, end, weight in routes:
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



    # Simple Version -- shortest path with BFS between 2 points 
    # We can find a shortest path with a modified version of BFS 
    # If we can keep a track of:
        # previous node where we came from 
        # distance from the start to every single node 

    def shortestPathBFS(self, start, end):
        visited = set()
        toVisit = [start]   

        prevDict = {key:None for key in self.undirectedGraph.keys()}
        distanceDict = {key:-1 for key in self.undirectedGraph.keys()}
        distanceDict[start] = 0

        while toVisit:
            
            currNode = toVisit.pop(0)
            
            for neighbor in self.directedGraph[currNode]: 
                if neighbor not in visited:
                    visited.add(neighbor)                           # remember, this comes here!
                    prevDict[neighbor] = currNode
                    distanceDict[neighbor] = distanceDict[currNode] + 1     # we medify this in Dijkstra
                    toVisit.append(neighbor) 
        
        # To get the shortest path -- go over the previousDict in reverse and reach the start 
        shortestPath = []

        while end != start:
            shortestPath.append(end)
            end = prevDict[end]

        shortestPath.append(start)
        shortestPath.reverse()
        
        return shortestPath

    # The dijkstra algorithm (at its core) gives us a shortest tree. i.e., given a start node,
    # it returns the shortest distance to every other node in the graph 
    # We can update the algorithm to stop at end node accordingly 

    # Steps are similar to modified-BFS
    # We need a distDict along with prevDict



# Input Format 
# 1. We are given the routes only 
routes = [["A", "B", 2], ["A", "D", 5], ["D", "C", 3], ["D", "E", 2], ["B", "C", 1], 
["A", "C", 4], ["C", "E", 2], ["E", "G", 1], ["D", "G", 4]]
listGraph = GraphList()

listGraph.populateDirectedGraph(routes) 
print("Directed Graph:  ")
listGraph.printDirectedGraph()

listGraph.populateUndirectedGraph(routes)
print("\nUn-directed Graph:  ")
listGraph.printUndirectedGraph()


######### Target 1:  Find the shortest path between 2 nodes
# startNode = "A"
# endNode = "G"
# print("\nShortest Path: ")
# print(listGraph.shortestPathBFS(startNode, endNode))    # shortest = ACF, longest = ABCF, ADEF 


































# Adjacency Matrix Implementation 
class GraphMatrix:
    def __init__(self):
        pass 