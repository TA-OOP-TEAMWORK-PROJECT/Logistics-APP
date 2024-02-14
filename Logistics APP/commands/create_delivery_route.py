from datetime import timedelta
from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData
from models.distances import CitiesDistances
from validation_helpers import parse_departure_time

class CreateDeliveryRouteCommand:
    def __init__(self, params:list [str], app_data:ApplicationData):
        validate_params_count(params, 4)
        self.params = params
        self._app_data = app_data
        self.distances = CitiesDistances()

    def execute(self, params):
        start = params[0]
        end = params[1]
        route = self._app_data.create_route(start, end)
        route.route = self.add_locations()
        return f'Route with {route.route_id} was created!'

    def add_locations(self):
        first_start = input()
        possible_route = {first_start: parse_departure_time()}
        prev_city = first_start
        command = input()

        while not command == 'end':
            distance = self.distances.get_distance(prev_city, command)
            travel_time = self._app_data.calculate_eta(distance)
            next_arr_time = self.assign_arrival_times(possible_route[prev_city], travel_time) #Времето на което е бил преди това, времето за което трябва да стигне до дестинацията
            possible_route[command] = next_arr_time
            prev_city = command
            command = input()

        return possible_route

    @staticmethod
    def assign_arrival_times(prev_city_time, travel_time):
        new_time = prev_city_time + travel_time
        if new_time.hour > 20 or (new_time - prev_city_time).days > 0:
            new_time = new_time.replace(hour=6, minute=0) + timedelta(days=1)
        return new_time
