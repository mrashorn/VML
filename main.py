# VML main.py - the main loop to run the CLI Vehicle Maintenance Log
import sys


class VehicleMaintenanceLog:
    """Overall class to manage the Vehicle Maintenance Log."""

    def __init__(self):
        """Initialize the log and load all vehicle data."""
        print("Welcome to the VML - Vehical Maintenance Log.\n")

    def run_vml(self):
        """Main loop of the VML."""
        print("We are in the main loop of the VML.\n")
        


if __name__ == '__main__':
    # Run the VML. 
    vml = VehicleMaintenanceLog()
    vml.run_vml()
    print("OK LEAVING MAIN.")
