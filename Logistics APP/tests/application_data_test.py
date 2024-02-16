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

class ApplicationData_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()

    def test_properties_returnCorrectTypes(self):
        self.assertIsInstance(self.app_data.customers, tuple)
        self.assertIsInstance(self.app_data.packages, tuple)
        self.assertIsInstance(self.app_data.routes, tuple)
        self.assertIsInstance(self.app_data.trucks, list)

    def test_create_customer(self):
        self.app_data.create_customer("Pesho", "0879556677")
        self.assertEqual(len(self.app_data.customers), 1)
        self.assertIsInstance(self.app_data.customers[0], Customer)

    def test_find_customer_by_number(self):
        self.app_data.create_customer("Pesho", "0879556677")
        customer = self.app_data.find_customer("0879556677")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Pesho")

    def test_create_package(self):
        self.app_data.create_customer("Kireto", "0879158666")
        package = self.app_data.create_package("Adelaide", "Sydney", 100, Customer)
        self.assertEqual(len(self.app_data.packages), 1)
        self.assertIsInstance(package, Package)




if __name__ == '__main__':
    unittest.main()
