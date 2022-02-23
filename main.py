# Kyle Green Student ID: #001363834

from DataRetrieval import DistanceData
from DataRetrieval import PackageData
from WGUPSClasses import Truck
from WGUPSClasses import TruckLoader
from UI import UserInterface
from WGUPSClasses import PackageDeliverer

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

DData = DistanceData.DistanceData()
PData = PackageData.PackageData()
PDeliverer = PackageDeliverer.PackageDeliverer()

# Get data from CSV files
DData.set_distance_data()
# Build graph of addresses
address_graph = DData.get_distance_data()
vertex_map = DData.get_vertex_map()
hub_vertex = vertex_map['4001 South 700 East']
# Build hashtable of all packages
PData.set_package_data(vertex_map)
package_list = PData.get_package_data()
package_9 = package_list.search_by_id(9)
updated_address = '410 S State St'
package_9.delivery_address = updated_address
package_9.address_vertex = vertex_map[updated_address]
# Create Truck objects
truck1 = Truck.Truck(1, 'John', vertex_map, address_graph)
truck2 = Truck.Truck(2, 'Jim', vertex_map, address_graph)
# Initialize TruckLoader class
TruckLoader = TruckLoader.TruckLoader(truck1, truck2, package_list)


# Load packages that have deadlines before 10:30 AM.
def load_early_packages():
    TruckLoader.load_early_deadlines()
    truck1.generate_address_list()
    truck2.generate_address_list()
    return PDeliverer.create_delivery_route(truck1.current_location, truck1.address_list, truck1.address_graph),\
        PDeliverer.create_delivery_route(truck2.current_location, truck2.address_list, truck2.address_graph)


# Load packages with no special notes or requirements.
def load_trucks():
    TruckLoader.load_packages()
    truck1.generate_address_list()
    truck2.generate_address_list()
    return PDeliverer.create_delivery_route(truck1.current_location, truck1.address_list, truck1.address_graph),\
        PDeliverer.create_delivery_route(truck2.current_location, truck2.address_list, truck2.address_graph)


# Load packages that were delayed on a flight and couldn't be picked up until 9:05.
def load_delayed():
    TruckLoader.load_delayed_packages()
    truck1.generate_address_list()
    truck2.generate_address_list()
    return PDeliverer.create_delivery_route(truck1.current_location, truck1.address_list, truck1.address_graph),\
        PDeliverer.create_delivery_route(truck2.current_location, truck2.address_list, truck2.address_graph)


# Return to the hub and load packages after first delivery routes.
def return_load():
    TruckLoader.load_rest_of_packages()
    truck1.generate_address_list()
    truck2.generate_address_list()
    return PDeliverer.create_delivery_route(truck1.current_location, truck1.address_list, truck1.address_graph),\
        PDeliverer.create_delivery_route(truck2.current_location, truck2.address_list, truck2.address_graph)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Load and deliver early packages and deliver first.
    early_route_1 = load_early_packages()
    early_route_2 = load_trucks()
    PDeliverer.deliver_packages(truck1, early_route_2[0])
    PDeliverer.deliver_packages(truck2, early_route_2[1])

    # Have truck 2 return to hub to pick up the delayed packages.
    truck2.return_to_hub()
    delayed_route = load_delayed()
    updated_route = load_trucks()
    PDeliverer.deliver_packages(truck1, updated_route[0])
    PDeliverer.deliver_packages(truck2, updated_route[1])
    truck1.return_to_hub()
    truck2.return_to_hub()

    # Load and deliver another set of packages after early morning deliveries.
    delivery_route_1 = return_load()
    PDeliverer.deliver_packages(truck1, delivery_route_1[0])
    PDeliverer.deliver_packages(truck2, delivery_route_1[1])

    # Return to Hub after trucks have delivered all their packages and load trucks again.
    truck1.return_to_hub()
    truck2.return_to_hub()

    delivery_route_2 = return_load()
    PDeliverer.deliver_packages(truck1, delivery_route_2[0])
    PDeliverer.deliver_packages(truck2, delivery_route_2[0])

    # Initialize and show UI
    UI = UserInterface.UserInterface(package_list, truck1, truck2)
    UI.show_main_menu()
