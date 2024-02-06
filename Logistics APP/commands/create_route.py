from commands.validation_helpers import validate_params_count
from models.route import Route
from core.application_data import ApplicationData

class CreateRouteCommand:
    def __init__(self, params:list [str], app_data:ApplicationData):
        validate_params_count(params , 4, "CreateRoute")
        self._params = params
        self._app_data = app_data

    def execute(self):
        start_location, end_location, departure_time, arrival_time = self._params

        self._app_data.create_route(start_location, end_location, departure_time, arrival_time)

        return f'Route with {Route.id} was created!'