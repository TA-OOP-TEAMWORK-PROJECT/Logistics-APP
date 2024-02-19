import unittest
from core.application_data import ApplicationData
from models.customer import Customer
from models.package import Package
from commands.create_package import CreatePackageCommand
from errors.invalid_params import InvalidParams


class CreatePackageCommand_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()
        self.customer = Customer("Kireto", "0877123456")
        self.app_data._customers.append(self.customer)

    def test_execute_CreatesNewPackageSuccessfully(self):
        # Arrange
        start_location = "Brisbane"
        end_location = "Perth"
        weight = 200
        params = [start_location, end_location, weight, self.customer.phone_number]

        # Act
        command = CreatePackageCommand(params, self.app_data)
        result_message = command.execute()

        created_package = self.app_data.daily_packages[-1]

        # Assert
        self.assertIsInstance(created_package, Package)
        self.assertEqual(created_package.start_location, start_location)
        self.assertEqual(created_package.end_location, end_location)
        self.assertEqual(created_package.weight, float(weight))
        self.assertEqual(created_package.customer, self.customer)
        self.assertIn(created_package, self.customer.packages)
        self.assertIn("Package with", result_message)

    def test_init_RaisesInvalidParamsError_when_InvalidParamsCount(self):
        # Arrange, Act & Assert
        with self.assertRaises(InvalidParams):
            CreatePackageCommand(['Sydney', 'Melbourne', 200], self.app_data)

    def test_execute_RaisesValueError_when_CustomerPhoneNumberIsInvalid(self):
        # Arrange
        params = ["Sydney", "Brisbane", 200, "123asd"]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            CreatePackageCommand(params, self.app_data).execute()

        self.assertIn('Invalid number!', str(context.exception))

    def test_execute_RaisesValueError_when_WeightIsNotValid(self):
        # Arrange
        params = ["Sydney", "Brisbane", "whatever", self.customer.phone_number]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            CreatePackageCommand(params, self.app_data).execute()

        self.assertIn('Can not turn to float number!', str(context.exception))

if __name__ == '__main__':
    unittest.main()
