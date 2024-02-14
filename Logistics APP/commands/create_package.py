from models.package import Package
from core.application_data import ApplicationData
from commands.validation_helpers import try_parse_float, validate_params_count
from models.customer import Customer

class CreatePackageCommand:

    def __init__(self, params:list[str], app_data: ApplicationData):
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location, end_location, weight, customer = self._params
        weight = try_parse_float(weight)
        customer = self._app_data.find_customer(self._params[3])
        package = self._app_data.create_package(start_location, end_location, float(weight), customer)
        customer.packages.append(package)

        return f'Package with {package.id} was created!'
