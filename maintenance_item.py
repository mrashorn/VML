# Maintenance Schedule for a vehicle. 
from options import maintenance_options

class Maintenance_Item:
    """A class representing each individual maintenance item."""

    def __init__(self, name, interval):
        """Initialize the maintenance item."""
        self.name = name
        self.interval = interval
        # self.last_service_mileage = x

