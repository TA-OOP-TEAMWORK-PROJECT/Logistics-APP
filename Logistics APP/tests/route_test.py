import unittest
from datetime import datetime, timedelta
from models.route import Route
from models.package import Package
from models.truck import Truck
from models.actros import Actros
from models.man import Man
from models.scania import Scania
from generate_id.id_generator import RouteIdGenerator, TruckIdGenerator, PackageIdGenerator
from models.distances import CitiesDistances


class Route_Should(unittest.TestCase):
    def setUp(self):
        self.start_location = "Sydney"
        self.end_location = "Melbourne"
        self.route = Route(self.start_location, self.end_location)
        self.package = Package("Sydney", "Melbourne", 1000, "Customer1")

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        # Arrange, Act & Assert
        self.assertEqual(self.route.start_location, self.start_location)
        self.assertEqual(self.route.end_location, self.end_location)
        self.assertIsNone(self.route.expected_arrival_time)
        self.assertIsNone(self.route.assigned_truck)

    def test_route_is_in_progress_IfItWorksProperly(self):
        # Arrange & Act
        self.route.departure_time = datetime.now() - timedelta(hours=1)
        self.route.expected_arrival_time = datetime.now() + timedelta(hours=1)

        # Assert
        self.assertTrue(self.route.is_in_progress())

    def test_save_to_file(self):
        self.route.save_to_file()

    def test_info(self):
        # Arrange
        info_str = self.route.info()

        # Act & Assert
        self.assertIsInstance(info_str, str)
        self.assertIn(self.start_location, info_str)
        self.assertIn(self.end_location, info_str)

if __name__ == '__main__':
    unittest.main()
