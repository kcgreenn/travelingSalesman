from Algorithms import NearestNeighbor

nn = NearestNeighbor.NearestNeighbor()


# A class for creating the delivery routes.
class PackageDeliverer:
    # Default class constructor, takes no parameters.
    def __init__(self):
        self.loaded_delayed_packages = False

    # Uses the nearest neighbor algorithm to create an efficient delivery route.
    def create_delivery_route(self, current_location, other_addresses, address_graph):
        route_list = []
        total_distance = 0
        while len(other_addresses) > 0:
            nearest_neighbor = nn.find_nearest_neighbor(current_location, other_addresses, address_graph)
            route_list.append(nearest_neighbor)
            total_distance += nearest_neighbor[1]
            current_location = nearest_neighbor[0]
            other_addresses.pop(nearest_neighbor[0])
        return route_list, total_distance

    # Moves the truck to the delivery address and returns to hub when the truck is empty.
    def deliver_packages(self, truck, delivery_route):
        for address in delivery_route[0]:
            truck.move_to_address(address[0])
            if (not self.loaded_delayed_packages) and truck.truck_hour >= 9 and truck.truck_minute >= 0 and truck.truck_id == 1:
                self.loaded_delayed_packages = True
                truck.return_to_hub()
                break
