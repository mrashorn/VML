# VML main.py - the main loop to run the CLI Vehicle Maintenance Log
import sys
from vehicle import Vehicle
import options


class VehicleMaintenanceLog:
    """Overall class to manage the Vehicle Maintenance Log."""

    def __init__(self):
        """Initialize the log and load all vehicle data."""
        print("Welcome to the VML - Vehical Maintenance Log.\n")
        self.vehicles = []
        self.main_menu_options = options.main_menu_options
        

    def run_vml(self):
        """Main loop of the VML."""
        while True:
            selection = self._display_main_menu()
            self._route_to_next(selection)


    def _add_vehicles_loop(self):
        """Prompt the user to add multiple vehicles to the VML."""
        ans = 'y'
        while ans == 'y':
            print("Let's add a vehicle.\n")
            self._add_vehicle()
            ans = input("Do you want to add another vehicle?[y\\n]: ")


    def _add_vehicle(self):
        """Add a new vehicle to the VML."""
        new_vehicle = Vehicle()
        print(f"Added the {new_vehicle.make} {new_vehicle.model}.")
        new_vehicle.save_data()
        self.vehicles.append(new_vehicle)


    def _list_vehicles(self):
        """Prints the list of vehicles in the VML to the user."""
        print("\nHere are the current logged vehicles:\n")
        if len(self.vehicles) == 0:
            print("You have no vehicles!\n")

        else:
            for vehicle in self.vehicles:
                vehicle.print_name()


    def _display_main_menu(self):
        """Display the main options for the VML."""
        for index, option in enumerate(self.main_menu_options):
            print(index + 1, option)
        print("q to quit.")

        ans = input("\nMake a selection and press Enter: ")
        if ans == 'q':
            sys.exit()
        if int(ans) > len(self.main_menu_options):
            print("\nNot a valid selection.\n")
            return None
            
        return int(ans)


    def _route_to_next(self, selection):
        """Send the VML to the selected option."""
        if selection == 1:
            self._list_vehicles()
        if selection == 2:
            self._add_vehicles_loop()
        if selection > 2: 
            print("\nThese options are coming soon!")

        



if __name__ == '__main__':
    # Run the VML. 
    vml = VehicleMaintenanceLog()
    vml.run_vml()
    print("OK LEAVING MAIN.")
