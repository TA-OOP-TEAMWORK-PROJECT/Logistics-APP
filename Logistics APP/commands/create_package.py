from commands.validation_helpers import validate_params_count
from models.package import Package
from core.application_data import ApplicationData

class CreatePackageCommand:

    def __init__(self, params:list[str], app_data: ApplicationData):
        validate_params_count(params, 3, 'CreatePackage')
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location, end_location, weight = self._params

        self._app_data.create_package(start_location, end_location, weight)

        return f'Package with {Package.id} was created!'