
class Vehicle:
    """A class representing any given vehicle."""

    def __init__(self):
        """Initialze the vehicle and it's attributes."""
        self._make_new_vehicle()


    def _make_new_vehicle(self):
        """Taking user inputs for new vehicle attributes."""
        self.make = input("What is the vehicle's make?: ")
        self.model = input("What is the vehicle's model?: ")
