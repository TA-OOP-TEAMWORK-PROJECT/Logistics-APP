import unittest
from core.application_data import ApplicationData
from commands.create_customer import CreateCustomerCommand

class CreateCustommerCommand_Should(unittest.TestCase):
    def setUp(self):
        self.app_data = ApplicationData()

    def test_execute_createsNewCustomerSuccessfully(self):
        command = CreateCustomerCommand(['Gosho', '0895666777'], self.app_data)
        result = command.execute()
        self.assertIn('New customer with name Gosho and number 0895666777 created!', result)
        self.assertIsNotNone(self.app_data.find_customer('0895666777'))

    def test_execute_throwsException_whenCustomerNumberExists(self):
        self.app_data.create_customer('Gosho', '0895666777')
        with self.assertRaises(ValueError) as context:
            command = CreateCustomerCommand(['Gosho', '0895666777'], self.app_data)
            command.execute()
        self.assertEqual(str(context.exception), 'Customer with that number already exists!')

    def test_init_throwsException_whenInvalidParamsCount(self):
        with self.assertRaises(ValueError) as context:
            CreateCustomerCommand(['John Doe'], self.app_data)
        self.assertIn('expected 2 parameters', str(context.exception))

    def test_execute_throwsException_whenParamsAreInvalid(self):
        with self.assertRaises(ValueError):
            command = CreateCustomerCommand(['', '1234567890'], self.app_data)
            command.execute()
        with self.assertRaises(ValueError):
            command = CreateCustomerCommand(['John Doe', ''], self.app_data)
            command.execute()

if __name__ == '__main__':
    unittest.main()
