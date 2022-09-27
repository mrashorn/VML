# Maintenance Schedule for a vehicle. 
from options import maintenance_options

class Maintenance_Item:
    """A class representing each individual maintenance item."""

    def __init__(self, name, interval, current_mileage):
        """Initialize the maintenance item."""
        self.name = name
        self.interval = interval
        self.service_history = []
        self._get_service_history(current_mileage)

    def _get_service_history(self, current_mileage):
        """Get the service history for this service item, or assume 0 if above below interval."""
        user_entry = ''
        while user_entry != 'q':
            user_entry = input(f"Enter the mileage for each {self.name} service that has been completed (q to quit): ")
            if user_entry.isnumeric() and int(user_entry) < current_mileage:
                self.service_history.append(int(user_entry))
            elif user_entry == 'q':
                break
            else:
                print("That is not a valid mileage.")
        if self.service_history == []:
            self.service_history.append(0)

        self.service_history.sort()

