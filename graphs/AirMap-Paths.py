  
from collections import defaultdict
  
class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    def addEdge(self, start, end):
        self.graph[start].append(end)
  
    def showGraph(self):
        print(self.graph)


    def DFSHelper(self, start, end, visited, path, res):
 
        visited[start]= True
        path.append(start)
 
        if start == end:
            if not res:
                res.append(path.copy())
            elif len(path) < len(res[-1]):
                res[-1] = path.copy()
        else:
            for neighbor in self.graph[start]:
                if visited[neighbor]== False:
                    self.DFSHelper(neighbor, end, visited, path, res)
                
        path.pop()
        visited[start]= False


    def printAllPaths(self, start, end):
        visited = {}
        visited = {k: False for k in self.graph.keys()}
        path = []
        paths = []
        self.DFSHelper(start, end, visited, path, paths)

        return paths
    
    
    # def falseDict(self, dict):
    #     for key, value in self.graph.items():
    #         dict[key] = False 
    #     return dict 



g = Graph(4)
g.addEdge('A', 'B')
g.addEdge('B', 'A')
g.addEdge('A', 'C')
g.addEdge('C', 'A')
g.addEdge('A', 'D')
g.addEdge('D', 'A')
g.addEdge('B', 'C')
g.addEdge('C', 'B')
g.addEdge('B', 'D')
g.addEdge('D', 'B')

g.showGraph()

start = "A" ; end = "D"
paths = g.printAllPaths(start, end)
print(paths)
