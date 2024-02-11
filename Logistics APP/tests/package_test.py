import unittest
from models.package import Package

class Package_Should(unittest.TestCase):
    def setUp(self):
        self.package = Package("Sydney", "Melbourne", 10, "Customer")

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        self.assertEqual(self.package._start_location, "Sydney")
        self.assertEqual(self.package._end_location, "Melbourne")
        self.assertEqual(self.package._weight, 10)
        self.assertEqual(self.package.customer, "Customer")
        self.assertIsNotNone(self.package.id)

    def test_start_location_setter_WhenGivenValidLocation(self):
        # Arrange & Act
        self.package.start_location = "Brisbane"

        # Assert
        self.assertEqual(self.package.start_location, "Brisbane")

    def test_start_location_setter_WhenGivenInvalidLocation(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.package.start_location = "Dreamland"

    def test_end_location_setter_WhenGivenValidLocation(self):
        # Arrange & Act
        self.package.end_location = "Adelaide"

        # Assert
        self.assertEqual(self.package.end_location, "Adelaide")

    def test_end_location_setter_WhenGivenInvalidLocation(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.package.end_location = "Dreamland"

    def test_weight_setter_WhenGivenValidValues(self):
        # Arrange & Act
        self.package.weight = 22000

        # Assert
        self.assertEqual(self.package.weight, 22000)

    def test_weight_setter_WhenGivenInvalidValues(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.package.weight = -1
        with self.assertRaises(ValueError):
            self.package.weight = 42001

    def test_weight_setter_WhenValueIsZero(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.package.weight = 0


    def test_info_method(self):
        # Arrange & Act
        expected_info = (f"Package ID: {self.package.id}, Start Location: Sydney, "
                         f"End Location: Melbourne, Weight: 10, "
                         f"Customer: Customer, Assigned Route: None")

        # Assert
        self.assertEqual(self.package.info(), expected_info)


