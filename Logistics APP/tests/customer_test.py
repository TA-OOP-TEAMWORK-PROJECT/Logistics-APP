import unittest
from models.customer import Customer

class Custome_Should(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Gosho", "0878587698")

    def test_initialization(self):
        # Arrange & Act & Assert
        self.assertEqual(self.customer.name, "Gosho")
        self.assertEqual(self.customer.phone_number, "0878587698")
        self.assertEqual(len(self.customer.packages), 0)

    def test_name_setter_valid(self):
        # Arrange & Act
        self.customer.name = "Gosho"

        # Assert
        self.assertEqual(self.customer.name, "Gosho")

    def test_name_setter_invalid(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.customer.name = ""

        with self.assertRaises(ValueError):
            self.customer.name = None

    def test_phone_number_valid(self):
        # Arrange & Act
        self.customer.phone_number = "0878587698"
        self.customer.phone_number = "12345678901234"

        # Assert
        self.assertEqual(self.customer.phone_number, "0878587698")
        self.assertEqual(self.customer.phone_number, "12345678901234")

    def test_phone_number_invalid_non_digit(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.customer.phone_number = "12345abc"

    def test_phone_number_LengthOutOfBounds(self):
        # Arrange & Act & Assert
        with self.assertRaises(ValueError):
            self.customer.phone_number = "123456789012345"