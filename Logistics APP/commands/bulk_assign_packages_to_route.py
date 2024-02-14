from datetime import datetime, date, timedelta
from core.application_data import ApplicationData
from models.distances import CitiesDistances
from create_delivery_route import CreateDeliveryRouteCommand


#create route (start_loc, end_loc, other, locations, start_time, estim_arr_time)

class BulkAssignPackagesToRouteCommand:      #Use Case 2
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = params[0]
        self.package_ids = params[1:] #не могат да да int  list(map(int, params[1:]))
        self.app_data = app_data
        self.distances = CitiesDistances()

    def execute(self):
        route = self.app_data.find_route(self.route_id)
        packages = self.checker_package_id()
        route_distance = self.distances.calculate_total_route_distance(route)
        package_load = sum([p.weight for p in packages])
        route.assigned_truck = self.assign_truck(route_distance,package_load)
        self.app_data.daily_packages = []
        return f'New route was created!'
    def checker_package_id(self): #Id, които са вуведени от employee. Предполага се,че то е преценило маршрута и зне кои idta да вземе.
        packages = []
        for i in self.package_ids:
            packages.append(self.app_data.find_package(i))
        return packages

    def assign_truck(self, distance, load):
        if (0 <= distance <= 8000) and ( 0 <= load <= 42000):
            truck_type = 'Scania'
            # return self.app_data.add_truck('Scania', truck_id=10001)

        elif (0 <= distance <= 10000) and (0 <= load <= 37000):
            truck_type = 'Man'
            # return self.app_data.add_truck('Scania', truck_id=10002)

        elif (0 <= distance <= 13000) and (0 <= load <= 26000):
            truck_type = 'Actros'
            # return self.app_data.add_truck('Scania', truck_id=10003)
        else:
            return 'No truck found'
        truck = self.app_data.add_truck(truck_type)
        return truck

    #
    # @staticmethod
    # def add_days_to_now(time1):
    #     time1 + timedelta(days=d)
    #
    #     if self.expected_arrival_time.hour >= 20:
    #         remaining_hours = self.expected_arrival_time.hour - 20
    #         next_day_start = self.expected_arrival_time.replace(hour=6) + timedelta(days=1)
    #         self.expected_arrival_time = next_day_start + timedelta(hours=remaining_hours)





        # responses = []
        # for pkg_id in self.package_ids:
        #     try:
        #         self.app_data.add_package_to_route(pkg_id, self.route_id)
        #         responses.append(f"Package {pkg_id} assigned to route {self.route_id}.")
        #     except ValueError as e:
        #         responses.append(str(e))
        # return "\n".join(responses)

    #В единя случай имаме конкретн пратка, а която търсим път. В другия ще итерираме пратките на деня и ще създаваме път