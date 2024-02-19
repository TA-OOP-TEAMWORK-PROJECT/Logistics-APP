from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class ViewRouteCommand:

    def __init__(self, params: list[str], app_data: ApplicationData):
        self.route_id = params[0]
        self._app_data = app_data

    def execute(self):
        route = self._app_data.find_route(self.route_id)
        if route:
            return route.info()
        else:
            return f"No route found with ID {self.route_id}"
