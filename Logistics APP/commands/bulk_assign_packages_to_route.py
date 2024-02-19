from core.application_data import ApplicationData
from models.distances import CitiesDistances


class BulkAssignPackagesToRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = params[0]
        self.package_ids = params[1:]
        self.app_data = app_data
        self.distances = CitiesDistances()

    def execute(self):
        route = self.app_data.find_route(self.route_id)
        packages = self.checker_package_id(route) #route?
        route_distance = self.distances.calculate_total_route_distance(route.route)
        package_load = sum([p.weight for p in packages])
        route.assigned_truck = self.app_data.assign_truck(route_distance, package_load)
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


    # def assign_truck(self, distance, load):
    #     if (0 <= distance <= 8000) and ( 0 <= load <= 42000):
    #         truck_type = 'Scania'
    #         # return self.app_data.add_truck('Scania', truck_id=10001)
    #
    #     elif (0 <= distance <= 10000) and (0 <= load <= 37000):
    #         truck_type = 'Man'
    #         # return self.app_data.add_truck('Scania', truck_id=10002)
    #
    #     elif (0 <= distance <= 13000) and (0 <= load <= 26000):
    #         truck_type = 'Actros'
    #         # return self.app_data.add_truck('Scania', truck_id=10003)
    #     else:
    #         return 'No truck found'
    #     truck = self.app_data.add_truck(truck_type)
    #     return truck
