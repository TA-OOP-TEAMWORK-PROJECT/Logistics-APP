from core.application_data import ApplicationData
from models.distances import CitiesDistances


class BulkAssignPackagesToRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = params[0]
        self.package_ids = params[1:]
        self.app_data = app_data
        self.distances = CitiesDistances()
        

    def execute(self):
        self.app_data.delivered_packages()
        route = self.app_data.find_route(self.route_id)
        packages = self.checker_package_id(route)
        route_distance = self.distances.calculate_total_route_distance(route.route)
        package_load = sum([p.weight for p in packages])

        truck = self.app_data.assign_truck(route_distance, package_load)
        truck.assign_to_route(route)
        route.assigned_truck = truck
        route.packages = packages
        self.app_data.daily_packages = []
        return self.info()

    def checker_package_id(self, route):
        packages = []
        for i in self.package_ids:
            current_package = self.app_data.find_package(i)
            if current_package:
                self.app_data.assign_package_to_route(current_package, route)
                packages.append(current_package)
        return packages


    def info(self):
        result = f'Packages assigned to route with id number {self.route_id}:\n'
        for i in self.package_ids:
            result += f'{i}\n'

        return result.strip()
