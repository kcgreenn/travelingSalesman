import csv
from WGUPSClasses import Package
from DataStructures import HashTable
from WGUPSClasses import TimeLog

Time = TimeLog.TimeLog()
Package = Package.Package


# A class for loading package data from a local csv file.
class PackageData:
    def __init__(self):
        self.package_list = HashTable.HashTable()

    # Open a csv file containing package data and load data into a hashtable.
    def set_package_data(self, vertex_map):
        # Get Package data from WGUPS Package File
        with open('WGUPS Package File.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    # create new package
                    package_id = row[0].strip()
                    package_address = row[1].strip()
                    address_vertex = vertex_map[package_address]
                    package_city = row[2].strip()
                    package_state = row[3].strip()
                    package_zipcode = row[4].strip()
                    package_deadline = row[5].strip()
                    package_weight = row[6].strip()
                    package_note = row[7].strip()
                    new_package = Package(package_id, package_address, package_deadline, package_city, package_state,
                                          package_zipcode, package_weight, package_note, address_vertex)
                    # add new package to the package list
                    self.package_list.insert(new_package)
                    line_count += 1
        return self.package_list

    # Returns the hash table containing all packages.
    def get_package_data(self):
        return self.package_list
