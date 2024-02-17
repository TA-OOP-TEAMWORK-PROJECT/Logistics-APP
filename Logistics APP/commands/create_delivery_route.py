from datetime import timedelta
from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData
from models.distances import CitiesDistances
from commands.validation_helpers import parse_departure_time


class CreateDeliveryRouteCommand:
    def __init__(self, params:list [str], app_data:ApplicationData):
        validate_params_count(params, 2)
        self.params = params
        self._app_data = app_data
        self.distances = CitiesDistances()

    def execute(self):
        completed_routes = self._app_data.completed_routes()
        start = self.params[0]
        end = self.params[1]
        new_route = self._app_data.create_route(start, end)
        new_route.route = self.add_locations()
        self._app_data._routes.append(new_route)
        return f'Route with {new_route.route_id} was created!'


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
            dep_time = new_time.replace(hour=6, minute=0) + timedelta(days=1)
            new_time = dep_time + travel_time
        return new_time
