# A vertex in a graph data structure. Represents an address on a map.
class Vertex:
    # Class constructor taking label and address strings.
    def __init__(self, label, address):
        self.label = label
        self.address = address


# A graph data structure. Represents a geographical map. Composed of Vertices connected by undirected edges.
class Graph(object):
    # Default class constructor with no parameters.
    def __init__(self):
        self.adjacency_list = {}    # A dictionary with vertex objects as keys and a list of neighbors as values.
        self.edge_weights = {}      # A dictionary containing the weights of all edges in the graph.

    # Adds a new vertex to the graph by appending a new list in the adjacency list.
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # Connect two vertices with a directed edge.
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # Connect two vertices with an undirected edge. Represented as two directed edges.
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
