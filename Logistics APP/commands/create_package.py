from validation_helpers import validate_params_count
from models.package import Package
from core.application_data import ApplicationData
from validation_helpers import try_parse_float

class CreatePackageCommand:

    def __init__(self, params:list[str], app_data: ApplicationData):
        validate_params_count(params, 3)
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location, end_location, weight, customer = self._params
        weight = try_parse_float(weight)
        package = self._app_data.create_package(start_location, end_location, float(weight),customer)
        customer.packages.append(package)

        return f'Package with {package.id} was created!'
