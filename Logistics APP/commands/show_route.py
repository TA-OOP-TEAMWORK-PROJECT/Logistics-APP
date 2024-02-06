from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count

class ShowPackagesCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        validate_params_count(params, 2, 'ShowRoute')
        self._params = params
        self._app_data = app_data

    def execute(self):
        star_location = self._params[0]
        end_location = self._params[1]
        route = self._app_data.show_route_by_start_end_location(star_location, end_location)
        return route.to_string()