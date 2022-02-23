

# A class for creating packages to be delivered.
class Package:
    # Constructor for the Package class. Takes all of the package info as parameters.
    def __init__(self, package_id, delivery_address, delivery_deadline, delivery_city, delivery_state,
                 delivery_zipcode, package_weight, special_note, address_vertex, delivery_status='at the hub'):
        self.package_id = package_id
        self.delivery_address = delivery_address
        if delivery_deadline == 'EOD':
            self.delivery_deadline = '11:59 PM'
        else:
            self.delivery_deadline = delivery_deadline
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zipcode = delivery_zipcode
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.special_note = special_note
        self.address_vertex = address_vertex
        self.left_facility_at = ''
        self.delivered_at = ''

    # The string method to format the package data for printing.
    def __str__(self):
        if self.delivery_deadline == '11:59 PM':
            deadline = 'EOD'
        else:
            deadline = self.delivery_deadline
        return 'Package ID: ' + self.package_id + ' - ' + self.delivery_address + ' - ' + self.delivery_city\
               + ' - ' + self.delivery_zipcode + ' - ' + self.package_weight + ' lbs - Due: ' + deadline\
                + ' - Status: ' + self.delivery_status
