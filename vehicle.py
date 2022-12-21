import json 
from random import randint
from maintenance_item import Maintenance_Item
from options import maintenance_options

class Vehicle:
    """A class representing any given vehicle."""

    def __init__(self, loaded_data=""):
        """Initialize the vehicle and it's attributes."""
        self._make_new_vehicle(loaded_data)


    def _make_new_vehicle(self, loaded_data):
        """Taking user inputs for new vehicle attributes."""
        if not loaded_data:
            self.make = input("What is the vehicle's make?: ")
            self.model = input("What is the vehicle's model?: ")

            while True:
                self.year = input("What is the vehicle's year?: ")
                if not self.year.isnumeric():
                    print("Invalid year.")
                    continue
                if int(self.year) > 1850:
                    break
                else:
                    print("Invalid year.")

            while True:
                self.miles = input("How many miles does this vehicle have?: ")
                if not self.miles.isnumeric():
                    print("Invalid mileage.")
                    continue
                if int(self.miles) >= 0:
                    self.miles = int(self.miles)
                    break
                else:
                    print("Invalid mileage.")

            self.unique_id = self._create_unique_id()
            self.name = f"{self.year} {self.make} {self.model}"
            self._create_maintenance_schedule()
            self._first_time_schedule_setup()
        else:
            self.__dict__ = loaded_data

            


    def get_name(self):
        """Returns the vehicles common name."""
        return(f"{self.name} with {self.miles} miles.")


    def save_data(self):
        """Saves the vehicle's data to a json file."""
        vehicle_file_name = f"{self.year}_{self.make}_{self.model}_{self.unique_id}.json"
        vehicle_file = open(f"vehicle_data/{vehicle_file_name}", 'w')
        json.dump(self.__dict__, vehicle_file, indent=4)
        vehicle_file.close()


    def _create_unique_id(self):
        """Creates a random string for the vehicle to ID it."""
        num_list = []
        for i in range(6):
            digit = str(randint(0, 9))
            num_list.append(digit)
        return "".join(num_list)


    def _create_maintenance_schedule(self):
        """Creates the maintenance schedule as a dict."""
        self.maintenance_schedule = {}
        index = 1
        for key, value in maintenance_options.items():
            item = Maintenance_Item(key, value, self.miles)
            self.maintenance_schedule[str(index)] = item.__dict__
            index += 1


    def display_maintenance_schedule(self):
        """Prints the nicely formatted maintenance schedule."""
        print(f"Maintenance Schedule for: {self.name}")
        for index, item_dict in self.maintenance_schedule.items():
            print(index.ljust(4), item_dict['name'].ljust(30), str(item_dict['interval']).ljust(10))


    def _first_time_schedule_setup(self):
        """Walk the user through changing the maintenance schedule of a new vehicle."""
        self.display_maintenance_schedule()
        answer = ''
        while answer != 'n':
            print("\nWould you like to change any of these maintenance intervals? [y\\n]")
            answer = input()
            if answer == 'y':
                answer = input("\nEnter the number of the item to change: ")
                if not answer.isnumeric():
                    answer = input("\nRe-enter the number of the item to change: [q to quit]")
                    if answer == 'q':
                        return
                self._change_maintenance_item_interval(answer)
            else:
                return


    def _change_maintenance_item_interval(self, index):
        """Change the service interval for a maintenance item."""
        while True:
            new_interval = input(f"Change the interval for {self.maintenance_schedule[index]['name']} from {str(self.maintenance_schedule[index]['interval'])} to: ")
            if not new_interval.isnumeric():
                print("Invalid interval.")
                continue
            if int(new_interval) > 0:
                break
            else:
                print("Invalid interval.")
        self.maintenance_schedule[index]['interval'] = int(new_interval)
        print(f"The {self.maintenance_schedule[index]['name']} interval has been changed to {self.maintenance_schedule[index]['interval']}.\n")


    def _enter_new_vehicle_previous_service(self):
        """User enters the last time these services were completed."""
        # If the mileage of the interval is larger than the vehicles current mileage, assume last service was 0 miles.
        print("Now let's enter the most previous time each item was serviced.\n")
        for index, item_dict in self.maintenance_schedule.items():
            print(index.ljust(4), item_dict['name'].ljust(30), str(item_dict['interval']).ljust(10))


    def add_service_to_vehicle(self):
        """Add service event to a vehicle's maintenance item."""
        for index, item_dict in self.maintenance_schedule.items():
            print(index.ljust(4), item_dict['name'].ljust(30))
        user_entry = input("Select which item you would like to enter a service for: ")

        # check for valid inputs
        service_mileage = input(f"What mileage was the {self.maintenance_schedule[user_entry]['name']} service completed?: ")
        self.add_service_to_item(user_entry, service_mileage) 


    def add_service_to_item(self, user_entry, service_mileage):
        """Add service to the service history of an item."""
        if service_mileage.isnumeric() and int(service_mileage) >= 0 and int(service_mileage) < self.miles:
            self.maintenance_schedule[user_entry]['service_history'].append(int(service_mileage))
            print(f"Added service at {service_mileage} to {self.maintenance_schedule[user_entry]['name']} to {self.name} {self.unique_id}.")
            self.maintenance_schedule[user_entry]['service_history'].sort()
        elif service_mileage == 'q':
            return print("No service was added.")
        else:
            return print("That is not a valid mileage.")


