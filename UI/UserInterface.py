from WGUPSClasses import TimeLog

timelog = TimeLog.TimeLog()


# A class for creating the user interface and handling user requests.
class UserInterface:
    # The class constructor. Takes a list of all packages and the trucks involved in delivering them.
    def __init__(self, package_list, truck1, truck2):
        self.package_list = package_list
        self.main_options = '\nWGUPS Package Delivery\n<1>View Package Status || <2>View All Packages at' \
                            ' a Given Time || <3>Total Distance Travelled || <4>Exit Program'
        self.main_prompt = 'Select an option from them menu(1-4):\t'
        self.package_id_prompt = 'Enter the package ID number:'
        self.time_prompt = 'Enter the time for the package status(in the form of XX:XX AM/PM):'
        self.truck1 = truck1
        self.truck2 = truck2

    # Shows the main menu of the program. The user will select an option from 1 - 4.
    def show_main_menu(self):
        print(self.main_options)
        user_selection = input(self.main_prompt)
        if user_selection == '1':
            self.show_status_menu()
        elif user_selection == '2':
            self.show_status_at_time_menu()
        elif user_selection == '3':
            self.show_total_miles()
        elif user_selection == '4':
            print('Exiting Program...')
        else:
            print('Unrecognized Option\n\n')
            self.show_main_menu()

    # Shows the status of a specific package at a given time
    def show_status_menu(self):
        self.clear_screen()
        package_id = input(self.package_id_prompt)
        time = input(self.time_prompt)
        package = self.package_list.search_by_id(package_id)
        try:
            if timelog.is_after(time, package.left_facility_at) and timelog.is_after(package.delivered_at, time):
                print('Package:', package.package_id, 'was en route at ', time)
            elif timelog.is_after(package.left_facility_at, time):
                print('Package:', package.package_id, 'was at the hub at ', time)
            elif timelog.is_after(time, package.delivered_at):
                print('Package:', package.package_id, 'was delivered at ', package.delivered_at)
        except (RuntimeError, ValueError, TypeError, IndexError):
            print('Incorrect Time Format Entered. Please use a XX:XX AM/PM Format')
        input('Press the enter key to return to main menu...')
        self.show_main_menu()

    # Show a prompt for the user to enter the time at which they would like to view package data.
    def show_status_at_time_menu(self):
        time = input(self.time_prompt)
        self.show_all_package_status_at_time(time)

    # Iterate through all packages and show their status at the specified time.
    def show_all_package_status_at_time(self, time):
        print('All Package Status at:', time)
        for i in range(1, 41):
            package = self.package_list.search_by_id(i)
            try:
                if timelog.is_after(time, package.left_facility_at) and timelog.is_after(package.delivered_at, time):
                    print('Package:', package.package_id, 'was en route at ', time)
                elif timelog.is_after(package.left_facility_at, time):
                    print('Package:', package.package_id, 'was at the hub at ', time)
                elif timelog.is_after(time, package.delivered_at):
                    print('Package:', package.package_id, 'was delivered at ', package.delivered_at)
                break
            except (RuntimeError, ValueError, TypeError, IndexError):
                print('Incorrect Time Format Entered. Please use a XX:XX AM/PM Format')
        input('Press the enter key to return to main menu...')
        self.show_main_menu()

    # Shows the total number of miles driven by both trucks over the day.
    def show_total_miles(self):
        print('\n\n')
        if timelog.is_after(self.truck1.final_package.delivered_at, self.truck2.final_package.delivered_at):
            print('Final package delivered at: ', self.truck1.final_package.delivered_at)
        else:
            print('Final package delivered at: ', self.truck2.final_package.delivered_at)
        print('Truck 1 Total Distance: ', '{:.2f}'.format(self.truck1.total_distance),
              'miles - Truck 2 Total Distance: ', '{:.2f}'.format(self.truck2.total_distance), 'miles')
        print('Total Distance of Both Trucks: ', '{:.2f}'.format(self.truck1.total_distance
                                                                 + self.truck2.total_distance), ' miles\n\n')
        input('Please press the enter key to return to main menu...')
        self.show_main_menu()

    # "Clears" the screen to make the UI more readable.
    def clear_screen(self):
        clear = '\n' * 100
        print(clear)
