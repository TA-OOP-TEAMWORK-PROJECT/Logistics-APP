from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class CreateCustomerCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(list(params), 2, 'CreateCustomerCommand')
        self._params = params
        self._app_data = app_data  

    def execute(self):
        name, number = self._params

        if not name or not number:
            raise ValueError("Name and number cannot be empty.")
        
        if self._app_data.find_customer(number):  
            raise ValueError('Customer with that number already exists!')  
        
        self._app_data.create_customer(name, number)
        
        return f'New customer with name {name} and number {number} created!'
