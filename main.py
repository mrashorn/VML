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
        self._save_data()


    def _add_vehicle(self):
        """Add a new vehicle to the VML."""
        new_vehicle = Vehicle()
        same_vehicle = self._check_if_vehicle_exists(new_vehicle)
        if not same_vehicle:
            print(f"Added the {new_vehicle.make} {new_vehicle.model}.")
            new_vehicle.save_data()
            self.vehicles.append(new_vehicle)
            self.selected_vehicle = new_vehicle
        else:
            print("Vehicle was not added to VML.")


    def _check_if_vehicle_exists(self, new_vehicle):
        for vehicle in self.vehicles:
            if (new_vehicle.make == vehicle.make and new_vehicle.model == vehicle.model
                and new_vehicle.year == vehicle.year):
                print("This vehicle may already exist in the VML.")
                print(vehicle.get_name())
                while True:
                    same_response = input("Is this the same vehicle that you are currently adding? (y/n)")
                    if same_response == 'y':
                        return True
                    if same_response == 'n':
                        return False
                    else:
                        continue

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
        return self._get_selection_loop(len(self.vehicles)+1)


    def _display_vehicle_menu(self):
        """Display the menu for the vehicle's options."""
        for index, option in enumerate(self.vehicle_menu_options):
            print(index + 1, option)
        print("q to quit.")
        selection = self._get_selection_loop(len(self.vehicle_menu_options))
        self._vehicle_menu_route_to_next(int(selection))


    def _get_selection_loop(self, max_options):
        """Loop that manages inputs and handles outputs of menu selections."""
        ans = self._get_menu_selection(max_options)

        while ans == "Not a number!" or ans == "Selection is too high!":
            print("Not a valid input!")
            ans = self._get_menu_selection(max_options)

        return ans

    def _get_menu_selection(self, max_options, ans=''):
        """Get a numerical selection input from user that is within menu range."""
        if not ans:
            ans = input("\nMake a selection and press Enter: ")
        while not ans.isnumeric():
            if ans == 'q':
                sys.exit()
            return "Not a number!"
        while int(ans) > max_options:
            return "Selection is too high!"
            
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
            input("Press any key to continue...")



    def _vehicle_menu_route_to_next(self, selection):
        """Route the VML to the selection the user made at the vehicle option menu."""
        self._clear_screen()
        selection_string = self.vehicle_menu_options[selection - 1]
        if selection_string == "Get Maintenance History":
            self.selected_vehicle.display_maintenance_schedule()
        elif selection_string == "Add a Completed Service to Vehicle":
            self.selected_vehicle.add_service_to_vehicle()
        elif selection_string == "Find Next Service for Vehicle":
            print("Find next service.")
        elif selection_string == "Delete Vehicle":
            self._delete_vehicle()
        elif selection_string == "Back to Main Menu":
            print("Returning to Main Menu")
        else:
            print("Not an option!")
        input("Press any key to continue...")


    def _delete_vehicle(self):
        """Deletes the selected vehicle from the VML."""
        # Delete the .json file for the vehicle
        for file in os.listdir("vehicle_data/"):
            if self.selected_vehicle.unique_id in file:
                print(f"Deleting {file}...")
                os.remove(f"vehicle_data/{file}")
        # delete the vehicle from the list of self.vehicles
        for vehicle in self.vehicles:
            if self.selected_vehicle.unique_id == vehicle.unique_id:
                print(f"Deleting {vehicle.get_name()} from vml.")
        self.vehicles[:] = [vehicle for vehicle in self.vehicles if vehicle.unique_id != self.selected_vehicle.unique_id]
        # clear self.selected_vehicle 
        self.selected_vehicle = None
        # return to Main Menu


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
