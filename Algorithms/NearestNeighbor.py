

# A class containing the nearest neighbor method.
class NearestNeighbor(object):
    # A nearest neighbor algorithm. Iterates through the list of edge_weights of the current location vertex.
    # Will return the vertex with the lowest weight(i.e. the shortest distance). Nearest neighbor algorithms
    # are able to achieve an approximate solution to the traveling salesman problem of finding the most efficient
    # route among multiple geographic locations.
    @staticmethod
    def find_nearest_neighbor(current_location, other_addresses, address_graph):
        smallest_distance = 1000
        nearest_neighbor = None
        for address in other_addresses:
            if address_graph.edge_weights[(current_location, address)] < smallest_distance:
                smallest_distance = address_graph.edge_weights[(current_location, address)]
                nearest_neighbor = address
        return nearest_neighbor, smallest_distance
