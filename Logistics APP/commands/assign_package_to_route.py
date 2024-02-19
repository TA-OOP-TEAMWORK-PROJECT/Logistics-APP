from commands.validation_helpers import validate_params_count
from core.application_data import ApplicationData


class AssignPackageToRouteCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(list(params), 2, 'AssignPackageToRouteCommand')
        self.route_id = params[0]
        self.package_id = params[1]
        self.app_data = app_data


    def execute(self):
        route = self.app_data.find_route(self.route_id)
        package = self.app_data.find_package(self.package_id)
        if route and package:
            try:
                self.check_destination_load(route, package)
                self.app_data.assign_package_to_route(package, route)
                return f"Package {self.package_id} assigned to route {self.route_id}."
            except:
                raise ValueError('No free space to load the package!')

    def check_destination_load(self, possible_route, package):

        pak = []
        some_destination_load = package.weight
        for k, v in possible_route.route.items():
            if k == package.end_location:
                break
            for i in possible_route.packages:
                if k == i.start_location:
                    pak.append(i)
                    some_destination_load += i.weight
                for end in range(len(pak)):
                    if k == pak[end].end_location:
                        some_destination_load -= pak[end].weight

        if some_destination_load <= (possible_route.assigned_truck.capacity_kg - some_destination_load):
            return some_destination_load
        raise ValueError('Not enough free space')




    # def check_destination_load(self, possible_route, package):
    #
    #     pak = []
    #     end_loc = []
    #     destination_load = package.weight
    #
    #     for k, v in possible_route.route.items():
    #         if k == package.end_location:
    #             break
    #
    #         for package in possible_route.packages:
    #             if k == package.start_location:
    #                 destination_load += package.weight
    #                 end_loc.append(package.end_location)
    #
    #             if k == package.end_location:
    #                 if
    #
    #         for end in range(len(end_loc)):
    #             if k == end_loc[end]:
    #                 destination_load -= pak[end].weight
    #
    #     if destination_load <= (possible_route.assigned_truck.capacity_kg - destination_load):
    #         return destination_load
    #     raise ValueError('Not enough free space')



