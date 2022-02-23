import csv
from DataStructures import Graph

Vertex = Graph.Vertex


# A class used to load distance data from a local csv file.
class DistanceData(object):
    def __init__(self):
        self.vertex_map = {}
        self.address_map = {}
        self.address_graph = Graph.Graph()

    # Open the file and store each line as a vertex in the address graph.
    # Also creates weighted edges between the vertices.
    def set_distance_data(self):
        with open('WGUPS Distance Table.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for index, row in enumerate(csv_reader):
                self.address_map[index] = row[1].strip()
                # Create a vertex for each delivery address, and add it to the Graph
                new_vertex = Vertex(row[0].strip(), row[1].strip())
                self.address_graph.add_vertex(new_vertex)
                self.vertex_map[row[1].strip()] = new_vertex
                # Add edges to all vertices with the distances as the edge weight.
                for i in range(2, len(row)):
                    # If the column is 0 or an empty value, do not create an edge.
                    if row[i].strip() == '0' or row[i].strip() == '':
                        pass
                    else:
                        self.address_graph.add_undirected_edge(new_vertex, self.vertex_map[self.address_map[i - 2]], float(row[i]))

    # Returns the address graph created from the distance data.
    def get_distance_data(self):
        return self.address_graph

    # Returns a map of vertices to the address string.
    def get_vertex_map(self):
        return self.vertex_map

    # Returns a map of addresses to indices.
    def get_address_map(self):
        return self.address_map
