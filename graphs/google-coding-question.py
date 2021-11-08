
'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

*** Understanding the Problem *** 

equation:   [Ai, Bi]    where Ai, Bi are strings 
values[i]:  Ai/Bi  

queries:    j --> [Cj, Dj]      
equation:   
i = 0        ["a", "b"], 
i = 1        ["c","a"],
  
values[i]:  i represent the value of equation[i][0]/ equation[i][1]


*** Example Case 1 *** 

equations = [["a","b"], ["b","c"]], 
values =      [2.0,         3.0], 

queries = [["a","c"], ["b","a"],  ["a","e"],  ["a","a"],   ["x","x"]]
Output:    [6.00000,   0.50000,  -1.00000,    1.00000,    -1.00000]

# Think in terms of currency:       a -> b = 2 ,   b --> 0.5 

'''


### *** Understanding the Problem *** ### 
# the points given can be converted into a undirected graph 

# Test Cases: 
    # a --> b (cost is 2)     b --> a (cost is 1/2) 
    # b --> c (cost is 3)     c --> b (cost is 1/3)
    # a --> c --> path is a ->b -> c    (cost is 2 * 3)

# Edge Cases:
    # If a node/currency does not exist --> return - 1 


# DFS vs BFS 
    # We wish to have a shortest path from one currency to the other to minimize our conversions 
    # We will choose BFS (Dijkstra?)


### *** Sub-Problems *** ### 
# 1. Construct a graph out of equations w.r.t. their values --> weighted + undirected graph
# 2. For each query, apply a DFS and find the shortest path


class Graph:
    def __init__(self, equations, values):
        self.graph = {}
        self.vertices = set()
        self.populateGraph(equations, values)

    def populateGraph(self, equations, values):
        for i in range(len(equations)):

            self.vertices.add(equations[i][0])
            self.vertices.add(equations[i][1])

            if equations[i][0] not in self.graph:
                self.graph[equations[i][0]] = [(equations[i][1], values[i])]
            else:
                self.graph[equations[i][0]].append((equations[i][1], values[i]))
            
            if equations[i][1] not in self.graph:
                self.graph[equations[i][1]] = [(equations[i][0], 1 / values[i])]
            else:
                self.graph[equations[i][1]].append((equations[i][0], values[i])) 

    def printGraph(self):
        print(self.graph)


    # {'a': [('b', 2.0)], 'b': [('a', 0.5), ('c', 3.0)], 'c': [('b', 0.3)]}

    # given a start and end node, we wish to return the currency exchange value 
    def BFSHelper(self, start, end):
        visited = set()
        toVisit = [start]
        costDict = {key:-1 for key in self.graph.keys()}
        costDict[start] = 1 

        while toVisit:
            currNode = toVisit.pop(0)
            visited.add(currNode)

            if currNode == end:
                return costDict[end] 
            else:
                for neighbor, neighborCost in self.graph[currNode]:
                    if neighbor not in visited:
                        toVisit.append(neighbor)

                        costDict[neighbor] = costDict[currNode] * neighborCost

        return -1 


    def resolveQueries(self, queries):
        res = []
        for start, end in queries:
            
            if start not in self.vertices or end not in self.vertices:
                res.append(-1)
            else:
                res.append(self.BFSHelper(start, end)) 

        return res 


# Main Function 
equations = [["a","b"], ["b","c"]] 
values =    [2.0, 3.0] 
queries = [["a","c"], ["b","a"],  ["a","e"],  ["a","a"],   ["x","x"]]

currencyGraph = Graph(equations, values)
currencyGraph.printGraph()
print(currencyGraph.resolveQueries(queries))

# Output:    [6.00000,   0.50000,  -1.00000,    1.00000,    -1.00000]
