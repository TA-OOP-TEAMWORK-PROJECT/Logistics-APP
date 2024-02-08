from validation_helpers import validate_params_count
from core.application_data import ApplicationData


class AssignPackageToRouteCommand:       #Use case 1
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2, 'AssignPackageToRoute')
        self.package_id, self.route_id = map(int, params)
        self.app_data = app_data

    def execute(self):
        try:
            self.app_data.add_package_to_route(self.package_id, self.route_id)
            return f"Package {self.package_id} assigned to route {self.route_id}."
        except ValueError as e:
            return str(e)