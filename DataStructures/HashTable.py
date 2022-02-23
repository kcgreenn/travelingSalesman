

# A hash table data structure. Uses a hashing algorithm to find the index of an item based on a unique id.
class HashTable:
    # Constructor with a default capacity parameter. For this project, the table will have a
    # default capacity of 40. Assign all indices with an empty array.
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Inserts a new package into the hashtable, at the appropriate bucket.
    def insert(self, new_package):
        # hash the package_id to find the correct bucket to insert into
        bucket = hash(new_package.package_id) % len(self.table)
        self.table[bucket].append(new_package)

    # Searches for the item with matching key in the hashtable.
    def search(self, package):
        # get the bucket where the package_id would be
        package_id = package.package_id
        bucket = hash(package_id) % len(self.table)
        # return either the matching package or None
        if package in self.table[bucket]:
            index = self.table[bucket].index(package)
            return self.table[bucket][index]
        else:
            # return None if package_id not found
            return None

    # Search for the item with the matching id
    def search_by_id(self, package_id):
        # get the bucket where the package_id would be
        bucket = hash(str(package_id)) % len(self.table)
        # return either the matching package or None
        for package in self.table[bucket]:
            if str(package_id) == package.package_id:
                return package
        return None

    # Removes a package with the matching package_id.
    def remove(self, package):
        # get the index where the package_id would be
        package_id = package.package_id
        bucket = hash(package_id) % len(self.table)

        if package in self.table[bucket]:
            self.table[bucket].remove(package)

