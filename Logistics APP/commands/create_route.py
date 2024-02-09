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
        route = self._app_data.create_route(start_location, end_location, departure_time) #arrival_time
        return f'Route with {route.route_id} was created!'

    def set_expected_arrival_time(self, arrival_time):
        self.expected_arrival_time = arrival_time



    def add_intermediate_stop(self, stop_location, expected_arrival_time):
        self.intermediate_stops.append({'location': stop_location, 'expected arrival time': expected_arrival_time})
        self.event_logs.append(EventLog(f"Stop added: {stop_location}."))

    def truck_is_compatible(self, truck):
        total_distance = self.calculate_route_distance()
        if total_distance > truck.max_range_km:
            return False
        if sum(package.weight for package in self.packages) + truck.current_load_kg > truck.capacity_kg:
            return False
        return True

    def calculate_location_distance(self, first_locstion, second_location):
        return self.distance.get_distance(first_locstion, second_location)


