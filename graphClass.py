import networkx as nx
import matplotlib.pyplot as plt
import pickle

class Vertex:
    def __init__(self, key, value):
      self.key = key
      self.value = value
      self.adjacent = {}
      self.n_adjacent = 0
      self.n_incident = 0
  
    def addEdge(self, vertex, weight = 0):
      if vertex.key in self.adjacent:
        return 'Vértice já existe'
      else:
        self.adjacent[vertex.key] = (vertex, weight)
        self.n_adjacent += 1
        vertex.n_incident += 1
  
    def removeEdge(self, vertex):
      if vertex.key in self.adjacent:
        del self.adjacent[vertex.key]
        self.n_adjacent -= 1
        vertex.n_incident -= 1
      else:
        return 'Vértice não existe'

    def redefineEdge(self, vertex, new_w):
      if vertex in self.adjacent:
        self.adjacent[vertex.key] = (vertex, new_w)

    def __repr__(self):
      return f"(Key: {self.key}, Value: {self.value})"


class Graph:
    def __init__(self):
      self.vertices = {}
      self.n_vertices = 0
      self.n_edges = 0

    def addVertex(self, key, value):
      if key in self.vertices:
        return 'Vértice já existe'
      else:
        vertex = Vertex(key, value)
        self.vertices[key] = vertex
        self.n_vertices += 1
  
    def removeVertex(self, key):
      if key in self.vertices:
        for vertex in self.vertices.values():
          if key in vertex.adjacent:
            del vertex.adjacent[key]
        del self.vertices[key]
        self.n_vertices -= 1
      else:
        return 'Vértice não existe no grafo'

    def addEdge(self, start_key, end_key, weight = 0, bidirectional = False):
      if start_key in self.vertices and end_key in self.vertices:
        con1 = self.vertices[start_key].addEdge(self.vertices[end_key], weight)
        self.n_edges += 1
        if bidirectional:
          con2 = self.vertices[end_key].addEdge(self.vertices[start_key], weight)
          self.n_edges += 1
      else:
        return 'Vértice não existe no grafo'

    def removeEdge(self, start_key, end_key, bidirectional = False):
      if (start_key in self.vertices) and (end_key in self.vertices):
        con1 = self.vertices[start_key].removeEdge(self.vertices[end_key])
        self.n_edges -= 1
        if bidirectional:
          con2 = self.vertices[end_key].removeEdge(self.vertices[start_key])
          self.n_edges -= 1
      else:
        return 'Vértice não existe no grafo'

    def inGraph(self, key):
      return key in self.vertices

    def neighbours(self, start_key, end_key, bidirectional = False):
      return (end_key in self.vertices[start_key].adjacent) or \
             (start_key in self.vertices[end_key].adjacent and bidirectional)

    def getAdjacent(self, key):
      if key in self.vertices:
        return [val[0] for val in self.vertices[key].adjacent.values()]
      else:
        return 'Vértice não existe'

    def getIncident(self, key):
      if key in self.vertices:
        incident = []
        for vertex in self.vertices.values():
          if key in vertex.adjacent:
            incident.append(vertex)
        return incident
      else:
        return 'Vértice não existe'
   
    def getEdgeWeight(self, start_key, end_key):
      if (start_key in self.vertices) and (end_key in self.vertices[start_key].adjacent):
        return self.vertices[start_key].adjacent[end_key][1]
      else:
        return None

    def getVertex(self, key):
        if key in self.vertices:
          return self.vertices[key]
        else:
          return None

    
    def BFS(self, start = None, visible = True, testFunction = None, max_level = None):
      if start:
        if start in self.vertices:
          start = self.vertices[start]
        else:
          return 'Vértice não existe'
      else:
        start = next(iter(self.vertices.values()))
    
      queue = [start]
      visited = dict.fromkeys(self.vertices.values(), 0)
      matches = []
      levels = dict.fromkeys(self.vertices.values(), None)
      levels[start] = 0
      while queue:
        vertex = queue[0]
        del queue[0]
        if not visited[vertex]:
          if visible:
            print(vertex)
          if (testFunction and testFunction(vertex)) or max_level != None:
              matches.append(vertex)
          visited[vertex] = 1

          for v in vertex.adjacent.values():
              if (max_level != None) and (not levels[vertex] < max_level):
                  pass
              else:
                  queue.append(v[0])
                  levels[v[0]] = levels[vertex] + 1
      return matches

    def DFS_rec(self, vertex, visible, visited, testFunction = None, matches = []):
      if not visited[vertex]:
        if visible:
            print(vertex)
        if testFunction and testFunction(vertex):
            matches.append(vertex)
        visited[vertex] = 1
        for v in vertex.adjacent.values():
          self.DFS_rec(v[0], visible, visited, testFunction, matches)
    
    def DFS(self, start, visible = True, testFunction = None):
      if start:
        if start in self.vertices:
          start = self.vertices[start]
        else:
          return 'Vértice não existe'
      else:
        start = next(iter(self.vertices.values()))
      matches = []
      self.DFS_rec(start, visible, visited = dict.fromkeys(self.vertices.values(), 0), testFunction = testFunction, matches = matches)
      return matches
    
    def getVertices(self):
        return self.vertices.keys()
    
    def getEdges(self):
        edges = []
        for key, v in self.vertices.items():
            if v:
                for key2, v2 in v.adjacent.items():
                    edges.append((key, key2, v2[1]))
        return edges
            
    

if __name__ == "__main__":      
        
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    g = Graph()
    vs = [g.addVertex(i, ls[i]) for i in range(1, 9)]
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 2)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(4, 8)
    g.addEdge(6, 5)
    g.addEdge(7, 2)
    g.addEdge(8, 7)

    g.getEdges()
  
