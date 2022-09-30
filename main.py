# VML main.py - the main loop to run the CLI Vehicle Maintenance Log
import sys, os, json
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
        # Load existing vehicle data from the start.
        self._fetch_vehicles()
        self._clear_screen()

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
        print("Here are the current logged vehicles:")

        for vehicle in self.vehicles:
            vehicle.print_name()


    def _fetch_vehicles(self):
        """Find all vehicles that are saved in the vehicle_data directory."""
        self._check_data_directory()
        if len(os.listdir("vehicle_data/")) < 1:
            print("No vehicles found in database during fetching.")
            return
        for file in os.listdir("vehicle_data/"):
            load_vehicle_data = json.load(open(f"vehicle_data/{file}", 'r'))

            self._add_loaded_vehicle(load_vehicle_data)


    def _add_loaded_vehicle(self, vehicle_data):
        """Add the loaded vehicle file to the active VML session / vehicle list."""
        new_vehicle = Vehicle(vehicle_data)
        self.vehicles.append(new_vehicle)


    def _check_data_directory(self):
        """Checks for vehicle_data/ directory. Creates it if it doesn't exist."""
        if os.path.exists('vehicle_data/'):
            return
        else:
            os.mkdir('vehicle_data/')


    def _display_main_menu(self):
        """Display the main options for the VML."""
        for index, option in enumerate(self.main_menu_options):
            print(index + 1, option)
        print("q to quit.")
        return self._get_menu_selection()


    def _get_menu_selection(self):
        """Get selection input from user."""
        ans = input("\nMake a selection and press Enter: ")
        while not ans.isnumeric():
            if ans == 'q':
                sys.exit()
            print("Not a number!")
            ans = input("\nMake a selection and press Enter: ")
            
        return int(ans)

    def _route_to_next(self, selection):
        """Send the VML to the selected option."""
        self._clear_screen()
        if selection > len(self.main_menu_options):
            print("Selection is out of range.\n")
            return
        selection_string = self.main_menu_options[selection - 1]
        if selection_string == "Display Vehicles":
            self._list_vehicles()
        elif selection_string == "Add Vehicle":
            self._add_vehicles_loop()
        elif selection_string == "Get Vehicle Maintenance History":
            self._display_vehicle_maint_schedules()
        elif selection_string == "Add a Completed Service to a Vehicle":
            self._add_completed_service()
        else:
            print("\nThis option is coming soon!")

        
    def _display_vehicle_maint_schedules(self):
        """Prompts the user for a vehicle, then displays the maint schedule for that vehicle."""
        # TO-DO: This is a quick function so I can keep printing the schedule without having to reload vehicles over and over 
        # during testing / building. 
        # this needs to be fixed to properly display the vehicle list and prompt the user which one to display the schedule of.
        for vehicle in self.vehicles:
            vehicle.display_maintenance_schedule()


    def _add_completed_service(self):
        """Adds a service to a specific vehicle, for a specific maintenance item."""
        index = 1
        for vehicle in self.vehicles:
            print(f"{index}. " + vehicle.name)
            index += 1
        user_entry = input("Select which vehicle to add a service to (1, 2, 3..): ")
        print("Adding service to " + self.vehicles[int(user_entry)-1].name)
        self.vehicles[int(user_entry)-1].add_service_to_vehicle()



    def _clear_screen(self):
        """clear the terminal screen."""
        os.system('clear')



if __name__ == '__main__':
    # Run the VML. 
    vml = VehicleMaintenanceLog()
    vml.run_vml()
