import json 
from random import randint
from maintenance_schedule import Maintenance_Schedule

class Vehicle:
    """A class representing any given vehicle."""

    def __init__(self, loaded_data=""):
        """Initialze the vehicle and it's attributes."""
        self._make_new_vehicle(loaded_data)


    def _make_new_vehicle(self, loaded_data):
        """Taking user inputs for new vehicle attributes."""
        if not loaded_data:
            self.make = input("What is the vehicle's make?: ")
            self.model = input("What is the vehicle's model?: ")
            self.year = input("What is the vehicle's year?: ")
            self.miles = int(input("How many miles does this vehicle have?: "))
            self.unique_id = self._create_unique_id()
            self.maintenance_schedule = self._create_maintenance_schedule()
        else:
            self.__dict__ = loaded_data
            


    def print_name(self):
        """Prints the vehicles common name."""
        print(f"{self.year} {self.make} {self.model} with {self.miles} miles.\n")


    def save_data(self):
        """Saves the vehicle's data to a json file."""
        vehicle_file_name = f"{self.year}_{self.make}_{self.model}_{self.unique_id}.json"
        vehicle_file = open(f"vehicle_data/{vehicle_file_name}", 'w')
        json.dump(self.__dict__, vehicle_file)
        vehicle_file.close()


    def _create_unique_id(self):
        """Creates a random string for the vehicle to ID it."""
        num_list = []
        for i in range(6):
            digit = str(randint(0, 9))
            num_list.append(digit)
        return "".join(num_list)


    def _create_maintenance_schedule(self):
        """Creates the maintenance schedule and returns it as a dict."""
        maint_schedule = Maintenance_Schedule()
        return maint_schedule.__dict__


        


