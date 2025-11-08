class Vertex():
    def __init__(self, data: int = None):
        self.data = data
        self.degree = 0
        self.neighbors = {}
        
class Edge():
    def __init__(self, u:Vertex, v: Vertex, weight: int = 1, bidirectional: bool = False):
        self.bidirectional = bidirectional
        self.weight = weight
        self.u = u
        self. v = v
        
class Graph():
    def __init__(self):
        self.root = None
        self.size = 0
        self.vertices = []
        self.edges = []
        self.adjacencylist = []
        
    def vertex_set(self):
        return self.vertices
    
    def edge_set(self):
        return self.edges

    def adjaceny_list(self):
        return self.adjacencylist
    
    def add(self, data: int) -> None:
        if self.size == 0:
            self.root = Vertex(data)
            self.vertices.append(self.root)
            return

        new_vertex = Vertex(data)
            
    def remove(self):
        pass

    def bfs():
        pass
    
    def dfs():
        pass
    
    
   