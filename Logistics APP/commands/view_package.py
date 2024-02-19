from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count

class ViewPackagesCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        validate_params_count(list(params), 2, 'ViewPackagesCommand')
        self._params = params
        self._app_data = app_data

    def execute(self):
        star_location = self._params[0]
        end_location = self._params[1]
        package = self._app_data.show_package_by_start_end_location(star_location, end_location)
        return package.info()
