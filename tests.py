# This test file is an exploration of adding unit tests 
# to the vml which has not been designed with testing in mind. 
# This is a learning exercise.
import unittest
import json
from vehicle import Vehicle


vehicle_data = json.load(open("test_F150_data.json", 'r'))

class Add_Service_Test_Case(unittest.TestCase):
    """Tests for vehicle.add_service()."""

    def test_test(self):
        """Just a test to see if it's working, auto pass."""
        self.assertEqual(1, 1)

    def test_vehicle_add_service_mileage_too_high(self):
        """Test to check if mileage of service is greater than vehicle miles."""
        vehicle_one = Vehicle(vehicle_data)
        vehicle_two = Vehicle(vehicle_data)
        vehicle_two.add_service_to_item(1, '999999999')
        self.assertEqual(vehicle_one.maintenance_schedule, vehicle_two.maintenance_schedule)

    def test_vehicle_add_service_proper_mileage(self):
        """Test to check if adding a service with proper mileage works."""
        vehicle_one = Vehicle(vehicle_data)
        vehicle_two = Vehicle(vehicle_data)
        vehicle_two.add_service_to_item(1, '400')
        self.assertNotEqual(vehicle_one.maintenance_schedule, vehicle_two.maintenance_schedule)
        

if __name__ == '__main__':
    unittest.main()

