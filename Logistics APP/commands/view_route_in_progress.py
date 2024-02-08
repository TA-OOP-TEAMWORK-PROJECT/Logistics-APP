from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count
from models.route import Route

class ViewRoutesInProgressCommand:          #Use case 3
    def __init__(self, app_data: ApplicationData):
        self.app_data = app_data

    def execute(self):
        routes_info = [route.info() for route in self.app_data._routes if route.is_in_progress()]
        return "\n".join(routes_info) if routes_info else "No routes in progress."