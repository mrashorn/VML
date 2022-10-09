# This test file is an exploration of adding unit tests 
# to the vml which has not been designed with testing in mind. 
# This is a learning exercise.
import unittest
import json
from vehicle import Vehicle
from main import VehicleMaintenanceLog 


vehicle_data_one = json.load(open("test_data/test_F150_data.json", 'r'))
vehicle_data_two = json.load(open("test_data/test_F150_data_2.json", 'r'))
# python passes by reference, so we can't use same data source!

class Add_Service_Test_Case(unittest.TestCase):
    """Tests for vehicle.add_service()."""

    def test_test(self):
        """Just a test to see if it's working, auto pass."""
        self.assertEqual(1, 1)

    def test_vehicle_add_service_mileage_too_high(self):
        """Test to check if mileage of service is greater than vehicle miles."""
        vehicle_one = Vehicle(vehicle_data_one)
        vehicle_two = Vehicle(vehicle_data_two)
        vehicle_two.add_service_to_item('1', '999999999')
        self.assertEqual(vehicle_one.maintenance_schedule, vehicle_two.maintenance_schedule)

    def test_vehicle_add_service_proper_mileage(self):
        """Test to check if adding a service with proper mileage works."""
        vehicle_one = Vehicle(vehicle_data_one)
        vehicle_two = Vehicle(vehicle_data_two)
        vehicle_two.add_service_to_item('1', '4000')
        self.assertNotEqual(vehicle_one.maintenance_schedule, vehicle_two.maintenance_schedule)

    def test_vehicle_add_service_negative_mileage(self):
        """Test negative mileage for service entry."""
        vehicle_one = Vehicle(vehicle_data_one)
        vehicle_two = Vehicle(vehicle_data_two)
        vehicle_two.add_service_to_item('1', '-4000')
        self.assertEqual(vehicle_one.maintenance_schedule, vehicle_two.maintenance_schedule)

    def test_vehicle_add_service_non_numeric_mileage(self):
        """Test negative mileage for service entry."""
        vehicle_one = Vehicle(vehicle_data_one)
        vehicle_two = Vehicle(vehicle_data_two)
        vehicle_two.add_service_to_item('1', 'word')
        self.assertEqual(vehicle_one.maintenance_schedule, vehicle_two.maintenance_schedule)


class Get_Menu_Selection_Test_Case(unittest.TestCase):
    """Tests for main._get_menu_selection()."""

    def test_selection_within_range(self):
        """Test to check if number passed as str within menu range gives selection."""
        log = VehicleMaintenanceLog()
        ans = log._get_menu_selection(3, '1') 
        self.assertEqual('1', ans)
        
    def test_selection_too_high(self):
        """Test to check if number passed as str outside menu range gives error."""
        log = VehicleMaintenanceLog()
        ans = log._get_menu_selection(3, '5')
        self.assertEqual(ans, "Selection is too high!")
 
    def test_selection_not_a_number(self):
        """Test to check if non-numerical string throws proper error."""
        log = VehicleMaintenanceLog()
        ans = log._get_menu_selection(3, 'dfjkjasdfad')
        self.assertEqual(ans, "Not a number!")
    
    def test_for_quit_input(self):
        """Test for sys.exit() if q is given to quit."""
        log = VehicleMaintenanceLog()
        try:
            ans = log._get_menu_selection(3, 'q')
            assert False
        except SystemExit:
            assert True

if __name__ == '__main__':
    unittest.main()

