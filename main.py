# VML main.py - the main loop to run the CLI Vehicle Maintenance Log
import sys, os, json
from vehicle import Vehicle
import options


class VehicleMaintenanceLog:
    """Overall class to manage the Vehicle Maintenance Log."""

    def __init__(self):
        """Initialize the log and load all vehicle data."""
        self.vehicles = []
        self.vehicle_menu_options = options.vehicle_menu_options
        self.selected_vehicle = None
        

    def run_vml(self):
        """Main loop of the VML."""
        # Load existing vehicle data from the start.
        self._fetch_vehicles()

        while True:
            selection = self._display_main_menu()
            self._main_select_vehicle(selection)
            self._display_vehicle_menu()
            self._save_data()


    def _add_vehicles_loop(self):
        """Prompt the user to add multiple vehicles to the VML."""
        ans = 'y'
        while ans == 'y':
            print("Let's add a vehicle.\n")
            self._add_vehicle()
            ans = input("Do you want to add another vehicle?[y\\n]: ")
        self._clear_screen()


    def _add_vehicle(self):
        """Add a new vehicle to the VML."""
        new_vehicle = Vehicle()
        print(f"Added the {new_vehicle.make} {new_vehicle.model}.")
        new_vehicle.save_data()
        self.vehicles.append(new_vehicle)


    def _list_vehicles(self):
        """Prints the list of vehicles in the VML to the user."""
        index = 1
        for vehicle in self.vehicles:
            print(f"{index}. " + vehicle.get_name())
            index += 1


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
        """Display the first menu, listing vehicles."""
        self._clear_screen()
        print("Welcome to the VML! Select a vehicle or add a new vehicle.")
        self._list_vehicles()
        print(str(len(self.vehicles)+1) +". Add a new vehicle.")
        print("q to quit.")
        return self._get_menu_selection(len(self.vehicles)+1)


    def _display_vehicle_menu(self):
        """Display the menu for the vehicle's options."""
        for index, option in enumerate(self.vehicle_menu_options):
            print(index + 1, option)
        print("q to quit.")
        selection = self._get_menu_selection(len(self.vehicle_menu_options))
        print(selection)
        input("Press any key to continue...")



    # OLD MAIN MENU, DELETE IF NOT NEEDED 
    def _display_old_main_menu(self):
        """Display the main options for the VML."""
        for index, option in enumerate(self.main_menu_options):
            print(index + 1, option)
        print("q to quit.")
        return self._get_menu_selection()


    def _get_menu_selection(self, max_options):
        """Get selection input from user."""
        ans = input("\nMake a selection and press Enter: ")
        while not ans.isnumeric():
            if ans == 'q':
                sys.exit()
            print("Not a number!")
            ans = self._get_menu_selection(max_options)
        while int(ans) > max_options:
            print("Selection is too high!")
            ans = self._get_menu_selection(max_options)
            
        return ans


    def _main_select_vehicle(self, selection):
        """Handle the selected option / vehicle from the main menu."""
        self._clear_screen()
        if int(selection) <= len(self.vehicles):
            self.selected_vehicle = self.vehicles[int(selection)-1]
            print(self.selected_vehicle.get_name() + " has been selected.")
        elif int(selection) == (len(self.vehicles)+1):
            self._add_vehicles_loop()
        else:
            print("In the last else loop of _main_selection_vehciles.")
            input("Press any key to continue!")



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


    def _save_data(self):
        """Save data for all vehicles."""
        for vehicle in self.vehicles:
            vehicle.save_data()



if __name__ == '__main__':
    # Run the VML. 
    vml = VehicleMaintenanceLog()
    vml.run_vml()
