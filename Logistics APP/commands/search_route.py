from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count

class SearchRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2, 'SearchRoute')
        self.start_location, self.end_location = params
        self.app_data = app_data

    def execute(self):
        route = self.app_data.show_route_by_start_end_location(self.start_location, self.end_location)
        if route:
            return f"Route from {self.start_location} to {self.end_location} found: {route.route_id}"
        else:
            return "No route found."