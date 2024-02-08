from core.application_data import ApplicationData


class AssignAllPackagesToRouteCommand:      #Use Case 2
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = int(params[0])
        self.package_ids = list(map(int, params[1:]))
        self.app_data = app_data

    def execute(self):
        responses = []
        for pkg_id in self.package_ids:
            try:
                self.app_data.add_package_to_route(pkg_id, self.route_id)
                responses.append(f"Package {pkg_id} assigned to route {self.route_id}.")
            except ValueError as e:
                responses.append(str(e))
        return "\n".join(responses)