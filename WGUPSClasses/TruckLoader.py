from WGUPSClasses import TimeLog

Time = TimeLog.TimeLog()


# A class for loading packages onto trucks.
class TruckLoader:
    # Class constructor. Takes truck objects and a list of all packages as parameters.
    def __init__(self, truck1, truck2, package_list):
        self.truck1 = truck1
        self.truck2 = truck2
        self.package_list = package_list
        self.truck_toggle = 1
        self.must_be_together = [13, 14, 15, 16, 19, 20]
        self.total_loaded_packages = 0
        self.current_truck = truck1

    # Load packages with deadlines before 10:30AM
    def load_early_deadlines(self):
        for i in range(1, 41):
            if self.truck1.number_of_packages > self.truck2.number_of_packages:
                self.current_truck = self.truck2
            else:
                self.current_truck = self.truck1
            current_package = self.package_list.search_by_id(i)
            if Time.is_after('10:31 AM', current_package.delivery_deadline) and \
                    current_package.delivery_status == 'at the hub':
                # Handle Special Note Instructions
                self.handle_special_notes(current_package)
            self.truck_toggle += 1

    # Load packages with no special restrictions.
    def load_packages(self):
        for i in range(1, 41):
            if self.truck1.number_of_packages > self.truck2.number_of_packages:
                self.current_truck = self.truck2
            else:
                self.current_truck = self.truck1
            current_package = self.package_list.search_by_id(i)
            # Handle Special Note Instructions
            self.handle_special_notes(current_package)
        self.truck_toggle += 1

    # Load packages that were delayed and not available before 9:05 AM
    def load_delayed_packages(self):
        for i in range(1, 41):
            if self.truck_toggle % 2 == 0 and not self.truck1.is_full():
                self.current_truck = self.truck1
            elif self.truck_toggle % 3 == 0 and not self.truck2.is_full():
                self.current_truck = self.truck2
            current_package = self.package_list.search_by_id(i)
            if current_package.special_note == 'Delayed on flight---will not arrive to depot until 9:05 am'\
                    and current_package.delivery_status == 'at the hub':
                # Handle special note instructions
                self.handle_special_notes(current_package)
            self.truck_toggle += 1

    # Load any packages that remain after all special cases.
    def load_rest_of_packages(self):
        for i in range(1, 41):
            if self.truck1.number_of_packages > self.truck2.number_of_packages:
                self.current_truck = self.truck2
            else:
                self.current_truck = self.truck1
            current_package = self.package_list.search_by_id(i)
            if current_package.delivery_status == 'at the hub' and not self.current_truck.is_full():
                # Handle special note instructions
                self.handle_special_notes(current_package)
            self.truck_toggle += 1

    # Handles all of the special notes on the packages.
    def handle_special_notes(self, current_package):
        if current_package.delivery_status == 'at the hub' and not self.current_truck.is_full():
            # Handle special note instructions
            # Handle packages that must be on the same truck.
            if int(current_package.package_id) in self.must_be_together and self.truck1.is_at_hub():
                self.truck1.load_package(current_package)
                self.total_loaded_packages += 1
            # Package #9 can't be delivered before 10:20 AM because the address will be updated then.
            elif current_package.package_id == '9' and Time.is_after('10:20 AM', self.current_truck.truck_time):
                pass
            elif current_package.package_id == '4':
                self.truck2.load_package(current_package)
            # Can't pick up delayed packages before 9:05
            elif Time.is_after('9:05 AM', self.current_truck.truck_time) and \
                    current_package.special_note == 'Delayed on flight---will not arrive to depot until 9:05 am':
                pass
            # Load truck 2 passage only on truck 2
            elif current_package.special_note == 'Can only be on truck 2' and self.truck2.is_at_hub():
                self.truck2.load_package(current_package)
                self.total_loaded_packages += 1
                self.current_truck.load_package(current_package)
                self.total_loaded_packages += 1
            elif self.current_truck.is_at_hub():
                self.current_truck.load_package(current_package)