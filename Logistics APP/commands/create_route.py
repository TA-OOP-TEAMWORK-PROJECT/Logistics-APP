from commands.validation_helpers import validate_params_count
from models.distances import CitiesDistances
from models.route import Route
from core.application_data import ApplicationData

class CreateRouteCommand:
    def __init__(self, params:list [str], app_data:ApplicationData):
        validate_params_count(params , 4)
        self._params = params
        self._app_data = app_data
        self.distance = CitiesDistances()

    def execute(self):
        start_location, end_location, departure_time, arrival_time = self._params
        route = self._app_data.create_route(start_location, end_location) #arrival_time
        return f'Route with {route.route_id} was created!'


