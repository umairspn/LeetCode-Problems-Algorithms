
# Weighted Graphs Implementation  


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
                self.directedGraph[start] = [(end, weight)]
            else:
                self.directedGraph[start].append((end, weight)) 

        for node in vertices:
            if node not in self.directedGraph:
                self.directedGraph[node] = []

    def printDirectedGraph(self):
        print(self.directedGraph)

    def populateUndirectedGraph(self, routes):
        for start, end, weight in routes:
            if start not in self.undirectedGraph:
                self.undirectedGraph[start] = [(end ,weight)]
            else:
                self.undirectedGraph[start].append((end, weight)) 
            
            if end not in self.undirectedGraph:
                self.undirectedGraph[end] = [(start, weight)]
            else:
                self.undirectedGraph[end].append((start, weight))

    def printUndirectedGraph(self):
        print(self.undirectedGraph)




    # # Simple Version -- shortest path with BFS between 2 points 
    # # We can find a shortest path with a modified version of BFS 
    # # If we can keep a track of:
    #     # previous node where we came from 
    #     # distance from the start to every single node 

    # def shortestPathBFS(self, start, end):
    #     visited = set()
    #     toVisit = [start]   

    #     prevDict = {key:None for key in self.undirectedGraph.keys()}
    #     distanceDict = {key:-1 for key in self.undirectedGraph.keys()}
    #     distanceDict[start] = 0

    #     while toVisit:
            
    #         currNode = toVisit.pop(0)
            
    #         for neighbor in self.directedGraph[currNode]: 
    #             if neighbor not in visited:
    #                 visited.add(neighbor)                           # remember, this comes here!
    #                 prevDict[neighbor] = currNode
    #                 distanceDict[neighbor] = distanceDict[currNode] + 1     # we medify this in Dijkstra
    #                 toVisit.append(neighbor) 
        
    #     # To get the shortest path -- go over the previousDict in reverse and reach the start 
    #     shortestPath = []

    #     while end != start:
    #         shortestPath.append(end)
    #         end = prevDict[end]

    #     shortestPath.append(start)
    #     shortestPath.reverse()
        
    #     return shortestPath








    # The dijkstra algorithm (at its core) gives us a shortest tree. i.e., given a start node,
    # it returns the shortest distance to every other node in the graph 
    # We can update the algorithm to stop at end node accordingly 

    # Steps are similar to modified-BFS
    # We need a distDict along with prevDict
    
    def DijkstraAlgorithm(self, startNode):
        paths = []
        toVisit = [startNode]        

        # distDict for storing the shortest distance for each node form the startPoint
        # prevDict for storing the previous node where we (path) came from        
        distanceDict = {key:float("inf") for key in self.directedGraph.keys()}
        distanceDict[startNode] = 0 
        prevDict = {key:None for key in self.directedGraph.keys()}
        visited = set()
        
        while toVisit:
            currNode = toVisit.pop(0)  
            visited.add(currNode)

            # How to pring the SHORTEST path? 
            # paths.append(currNode)

            for neighbor, neighborCost in self.directedGraph[currNode]:
                if neighbor not in visited:
                    toVisit.append(neighbor)

                    prevDict[neighbor] = currNode

                    # updating the shortest cost for every neighbor node 
                    currentDistance = distanceDict[currNode] + neighborCost
                    if currentDistance < distanceDict[neighbor]:
                        distanceDict[neighbor] = currentDistance

        print(distanceDict)
        print(prevDict)


    
    # Final Implementation of Dijkstra Algorithm 
    def dijkstraPaths(self, startNode, endNode):
        
        # when a node is visited, it goes to visited set so we don't visit it again 
        visited = set()
        
        # the breadth/neighbor nodes to visit in each go  
        toVisit = [startNode]

        # prevDict: store previous of each node 
        prevDict = {key:None for key in self.undirectedGraph.keys()}

        # distDict: dict that will store the min cost distance from start to each vertex 
        distDict = {key:float("inf") for key in self.undirectedGraph.keys()}
        
        # distance of startNode to itself is 0 
        distDict[startNode] = 0                                 

        while toVisit:
            currNode = toVisit.pop(0)

            # only when a node is popped from queue >> we add it to visited >> not during the neighbors 
            # it means >> we have processed the node completely, and then say it's visited >> so neighbor node can 
            visited.add(currNode)

            for neighbor, neighborCost in self.undirectedGraph[currNode]:
                if neighbor not in visited:
                    toVisit.append(neighbor)
                    
                    # update the shortest distance of each neighbor 
                    # neighbor's previous node is the currNode -- since neighbor is currNode child  
                    currDistance = distDict[currNode] + neighborCost 

                    if currDistance < distDict[neighbor]:
                        prevDict[neighbor] = currNode
                        distDict[neighbor] = currDistance

        print(prevDict) 
        print(distDict)

        # should be: [path = ABCE, cost = 6]  
        shortestPath = []

        end = endNode
        while end != None:
            shortestPath.append(end)
            end = prevDict[end]
        
        shortestPath.reverse()
        return shortestPath



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



######### Target 1:  Find the shortest path in weighted graph with Dijkstra Algorithm 

# Part A:   Given a start node, return the shortest distance to all other vertices of the graph 
startNode = "A"
endNode = "G"
print("\nDijkstra Algorithm Shortest Path from startNode ", startNode)
# print(listGraph.DijkstraAlgorithm(startNode))

print(listGraph.dijkstraPaths(startNode, endNode))





