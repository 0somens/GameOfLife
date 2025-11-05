# G = {S: ['A','B','C','D']}

# https://www.youtube.com/watch?v=S2kxjgQKRYk


class Directed_graph:
    def __init__(self):
        self.graph_dict = {}
    def add_vertex(self,vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = [] # G[v1] = []
    
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)
    
    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict
    
    # Busca un nodo por su nombre tipo str y debolverlo tipo obj nodo
    def get_vertex (self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name(): 
                return v
        print(f'Vertex {vertex_name} does not exist ')
        
    
    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + ' ----> ' + v2.get_name() + ' \n' 
        return all_edges
                

        
class Edge:
    def __init__(self,v1,v2): 
        self.v1 = v1
        self.v2 = v2
        
    def get_v1(self): #Regresarnos el nodo
        return self.v1
    
    def get_v2(self):
        return self.v2
# getters y setters
    def __str__(self):
        return self.v1.get_name() + ' ---> ' + self.v2.get_name() 
    
    
class Vertex: 
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    # ??? son lo mismo xD, bueno cosas del youtuber
    def __str__(self):
        return self.name
    
    
    
class Undirected_graph(Directed_graph):
    def add_edge(self, edge):
        Directed_graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2()), edge.get_v1()
        Directed_graph.add_edge(self,edge_back)
    
    
    
def build_graph(graph):
    g = graph()
    for v in ('s', 'a','b','c','d','e','f','g','i','x'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('a')))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('b')))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('c')))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('d')))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('d')))
    g.add_edge(Edge(g.get_vertex('a'), g.get_vertex('b')))
    g.add_edge(Edge(g.get_vertex('w'), g.get_vertex('g')))

    return g
        
        
G1 = build_graph(Directed_graph)
print(G1)
# G1 = build_graph(Undirected_graph)
    
    
    