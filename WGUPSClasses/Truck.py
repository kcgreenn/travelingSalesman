from Algorithms import NearestNeighbor
from DataRetrieval import DistanceData
from WGUPSClasses import TimeLog
import math

TimeLog = TimeLog.TimeLog()
DData = DistanceData.DistanceData()
nn = NearestNeighbor.NearestNeighbor


# A class for storing truck data and performing delivery actions.
class Truck:
    # Constructor of the Truck class. Takes driver as a parameter, and creates an empty list of packages.
    def __init__(self, truck_id, driver, vertex_map, address_graph, max_capacity=16, average_speed=18):
        self.truck_id = truck_id
        self.driver = driver
        self.max_capacity = max_capacity            # The maximum number of packages a truck can hold at one time.
        self.average_speed = average_speed          # average speed of the truck is 18 miles per hour
        self.current_packages = []                  # A list containing the packages loaded on to the truck.
        self.number_of_packages = 0                 # The number of packages currently on the truck
        self.current_location = vertex_map['4001 South 700 East']  # Location when instantiated is at the hub.
        self.address_graph = address_graph
        self.vertex_map = vertex_map
        self.address_list = {}
        self.truck_hour = 8
        self.truck_minute = 0
        self.truck_time = TimeLog.format_current_time(self.truck_hour, self.truck_minute)
        self.total_distance = 0
        self.final_package = None

    # Add a package to the package_list and increment current_packages. If truck is full return None.
    def load_package(self, package):
        if self.is_full() or package.delivery_status != 'at the hub':
            return None
        else:
            self.current_packages.append(package)
            self.number_of_packages += 1
            package.delivery_status = 'en route'
            package.left_facility_at = self.truck_time

    # Deliver a package to its address and decrement current_packages
    def deliver_package(self, package):
        self.current_packages.remove(package)
        self.number_of_packages = self.number_of_packages - 1
        package.delivery_status = 'delivered'
        package.delivered_at = self.truck_time
        self.final_package = package

    # Determine if the truck is filled to capacity.
    def is_full(self):
        return self.number_of_packages >= self.max_capacity

    # Determine if truck is at the hub, so it can load packages.
    def is_at_hub(self):
        return self.current_location is self.vertex_map['4001 South 700 East']

    def return_to_hub(self):
        hub_vertex = self.vertex_map['4001 South 700 East']
        # print(self.current_location.address)
        self.move_to_address(hub_vertex)
        # print('Truck: ', self.truck_id, 'returned to hub at ', self.truck_time)

    def move_to_address(self, next_vertex):
        # Update the total distance travelled by this truck
        if self.current_location is not next_vertex:
            distance = self.address_graph.edge_weights[(self.current_location, next_vertex)]
            self.total_distance += distance
            # Calculate time to get to Hub
            minutes = TimeLog.calculate_minutes_from_distance(self.average_speed, distance)
            hours = 0
            if minutes > 60:
                hours = math.floor(minutes / 60)
                minutes = minutes % 60
            # Update the time of day
            time_tuple = TimeLog.increment_current_time(self.truck_hour, self.truck_minute, hours, minutes)
            self.truck_hour = time_tuple[0]
            self.truck_minute = time_tuple[1]
            self.truck_time = TimeLog.format_current_time(self.truck_hour, self.truck_minute)
            # set current_location to new vertex, pass time
            self.current_location = next_vertex
            # Find package for current address and add to list for current address. Removing from package list caused an
            # error that would skip over the next package because its index would be reduced by 1.
            deliver_to_this_address = []
            for package in self.current_packages:
                if package.address_vertex.address == self.current_location.address:
                    deliver_to_this_address.append(package)
            for package in deliver_to_this_address:
                self.deliver_package(package)

    def generate_address_list(self):
        self.address_list = {}
        for package in self.current_packages:
            self.address_list[package.address_vertex] = package
