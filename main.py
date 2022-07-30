# VML main.py - the main loop to run the CLI Vehicle Maintenance Log
import sys
from vehicle import Vehicle


class VehicleMaintenanceLog:
    """Overall class to manage the Vehicle Maintenance Log."""

    def __init__(self):
        """Initialize the log and load all vehicle data."""
        print("Welcome to the VML - Vehical Maintenance Log.\n")
        self.vehicles = []
        

    def run_vml(self):
        """Main loop of the VML."""
        print("We are in the main loop of the VML.\n")
        print("Let's add a vehicle.\n")
        self._add_vehicle()


    def _add_vehicle(self):
        """Add a new vehicle to the VML."""
        new_vehicle = Vehicle()
        print(f"Our new vehicle is a {new_vehicle.make} {new_vehicle.model}!")



if __name__ == '__main__':
    # Run the VML. 
    vml = VehicleMaintenanceLog()
    vml.run_vml()
    print("OK LEAVING MAIN.")
