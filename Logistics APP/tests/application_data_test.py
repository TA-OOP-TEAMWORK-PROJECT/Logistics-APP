import unittest
from datetime import datetime, timedelta
from core.application_data import ApplicationData
from models.package import Package
from models.route import Route
from models.customer import Customer
from models.truck import Truck
from models.actros import Actros
from models.scania import Scania
from models.man import Man
from models.package_status import PackageStatus
from models.truck_status import TruckStatus
from models.distances import CitiesDistances
from commands.create_delivery_route import CreateDeliveryRouteCommand
class ApplicationData_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()

    def test_properties_returnCorrectTypes(self):
        # Arrange, Act & Assert
        self.assertIsInstance(self.app_data.customers, tuple)
        self.assertIsInstance(self.app_data.packages, tuple)
        self.assertIsInstance(self.app_data.routes, tuple)
        self.assertIsInstance(self.app_data.trucks, list)

    def test_create_customer_IfItCreatesACustomer(self):
        # Arrange & Act
        self.app_data.create_customer("Pesho", "0879556677")

        # Assert
        self.assertEqual(len(self.app_data.customers), 1)
        self.assertIsInstance(self.app_data.customers[0], Customer)

    def test_find_customer_by_number_IfItFindsTheRightCustomer(self):
        # Arrange & Act
        self.app_data.create_customer("Pesho", "0879556677")
        customer = self.app_data.find_customer("0879556677")

        # Assert
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Pesho")

    def test_create_package_IfItCreatesAPackages(self):
        # Arrange & Act
        customer = self.app_data.create_customer("Kireto", "0879158666")
        package = self.app_data.create_package("Adelaide", "Sydney", 100, customer)

        # Assert
        self.assertEqual(len(self.app_data.packages), 1)
        self.assertIsInstance(package, Package)

    def test_error_WhenCreatingPackageWithoutCreatingACustomer(self):        # Тествам след промените на Снежи.
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            self.app_data.create_package("Sydney", "Perth", 150, "what")

    def test_create_route_IfItCreatesARoute(self):
        # Arrange
        start_location = "Adelaide"
        end_location = "Sydney"

        # Act
        route = self.app_data.create_route(start_location, end_location)

        # Assert
        self.assertIsInstance(route, Route)
        self.assertEqual(route.start_location, start_location)
        self.assertEqual(route.end_location, end_location)

    def test_create_package_AndAssignItToRoute(self):                  #Чупи заради пакетите.
        # Arrange & Act
        customer = self.app_data.create_customer("Kireto", "0879158666")
        package = self.app_data.create_package("Adelaide", "Sydney", 100, customer)

        # Assert
        self.assertEqual(len(self.app_data.packages), 1)
        self.assertIsInstance(package, Package)

        # Arrange & Act
        route = self.app_data.create_route("Adelaide", "Sydney")
        self.app_data.assign_package_to_route(package.id, route.route_id)

        # Assert
        self.assertEqual(package.route, route)

    def test_assign_truck_to_route_BasedOnLoadAndDistance(self):
        # Arrange & Act
        self.app_data.create_route("Melbourne", "Brisbane")
        truck = self.app_data.assign_truck(13000, 20000)

        # Assert
        self.assertIsNotNone(truck)
        self.assertIn(truck, self.app_data.trucks)
        self.assertIsInstance(truck, Actros)
        self.assertNotIsInstance(truck, Man)
        self.assertNotIsInstance(truck, Scania)
        self.assertEqual(truck.truck_brand, "Actros")

    def test_view_unassigned_packages_IfItShowsThemWhenNotAsssignedToRoute(self):
        # Arrange & Act
        customer = self.app_data.create_customer("DonPepi", "0879158666")
        package1 = self.app_data.create_package("Brisbane", "Sydney", 1500, customer)
        package2 = self.app_data.create_package("Brisbane", "Sydney", 2000, customer)
        unassigned_packages = self.app_data.view_unassigned_packages()

        # Assert
        self.assertIn(package1, unassigned_packages)
        self.assertIn(package2, unassigned_packages)

    def test_package_delivery_UpdatesStatusWhenRouteIsComplete(self):           # Чупи, защото боравим с дейли пакети.
        # Arrange
        customer = self.app_data.create_customer("BatGiorgi", "0879158666")
        package = self.app_data.create_package("Brisbane", "Sydney", 1500, customer)
        route = self.app_data.create_route("Brisbane", "Sydney")

        # Act
        self.app_data.assign_package_to_route(package.id, route.route_id)
        self.app_data.delivered_packages(route)

        # Assert
        self.assertEqual(package.status, PackageStatus.DELIVERED)

    def test_routes_in_progress(self):
        # Arrange & Act
        self.app_data.create_route("Sydney", "Adelaide")
        in_progress_routes = self.app_data.view_routes_in_progress()

        # Assert
        self.assertGreaterEqual(len(in_progress_routes), 0)

    def test_truck_assignment_based_on_route_and_load_requirements(self):
        # Arrange & Act
        self.app_data.create_route("Sydney", "Brisbane")
        self.app_data.create_route("Adelaide", "Darwin")
        self.app_data.create_route("Perth", "Brisbane")

        scania_truck = self.app_data.assign_truck(7900, 41000)
        man_truck = self.app_data.assign_truck(9999, 30000)
        actros_truck = self.app_data.assign_truck(12000, 25000)

        # Assert
        self.assertIsInstance(scania_truck, Scania)
        self.assertIsInstance(man_truck, Man)
        self.assertIsInstance(actros_truck, Actros)

if __name__ == '__main__':
    unittest.main()
