import unittest
from core.application_data import ApplicationData
from commands.create_customer import CreateCustomerCommand
from errors.invalid_params import InvalidParams


class CreateCustommerCommand_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()

    def test_execute_createsNewCustomerSuccessfully(self):
        # Arrange
        command = CreateCustomerCommand(['Gosho', '0895666777'], self.app_data)

        # Act
        result = command.execute()

        # Assert
        self.assertIn('New customer with name Gosho and number 0895666777 created!', result)
        self.assertIsNotNone(self.app_data.find_customer('0895666777'))

    def test_execute_RaisesValueError_when_CustomerNumberExists(self):
        # Arrange
        self.app_data.create_customer('Gosho', '0895666777')

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            command = CreateCustomerCommand(['Gosho', '0895666777'], self.app_data)
            command.execute()
        self.assertEqual(str(context.exception), 'Customer with that number already exists!')

    def test_init_RaisesInvalidParamsError_when_InvalidParamsCount(self):
        # Arrange, Act & Assert
        with self.assertRaises(InvalidParams) as context:
            CreateCustomerCommand(['Gosho'], self.app_data)
        self.assertIn('CreateCustomerCommand command expects 2 parameters', str(context.exception))

    def test_execute_RaisesValueError_when_ParamsAreInvalid(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            command = CreateCustomerCommand(['', '0895666777'], self.app_data)
            command.execute()

        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            command = CreateCustomerCommand(['Gosho', ''], self.app_data)
            command.execute()


if __name__ == '__main__':
    unittest.main()
