import datetime

from commands.create_route import CreateRouteCommand
from core.application_data import ApplicationData
from models.distances import CitiesDistances


#create route (start_loc, end_loc, other, locations, start_time, estim_arr_time)

class BulkAssignPackagesToRouteCommand:      #Use Case 2
    def __init__(self, params, app_data: ApplicationData):
        self.route_id = params[0]
        self.package_ids = params[1:] #не могат да да int  list(map(int, params[1:]))
        self.app_data = app_data
        self.distances = CitiesDistances()

    def execute(self):
        route = self.add_locations()
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

    def add_locations(self): #С какво име влизат локациите?
        first_start = input()
        possible_route = {first_start: self.app_data.add_departure_time()}
        prev_city = first_start
        command = input()

        while not command == 'end':
            distance = self.distances.get_distance(prev_city, command)
            travel_time = self.app_data.calculate_eta(distance)
            next_arr_time = self.assign_arrival_times(possible_route[prev_city], travel_time) #Времето на което е бил преди това, времето за което трябва да стигне до дестинацията
            possible_route[command] = next_arr_time
            prev_city = command
            command = input()

    def assign_arrival_times(self, prev_city_time, travel_time):
        if (prev_city_time + travel_time).hours > 14 - prev_city_time.hour:
            prev_city_time.hour = 6
            prev_city_time.day += 1
        arr_time = prev_city_time + travel_time
        return arr_time

    def assign_truck(self, distance, load):

        if (0 <= distance  <= 8000) and ( 0 <= load <= 42000):
            return self.app_data.add_truck('Scania', truck_id=10001)

        if (0 <= distance <= 10000) and (0 <= load <= 37000):
            return self.app_data.add_truck('Scania', truck_id=10002)

        if (0 <= distance <= 13000) and (0 <= load <= 26000):
            return self.app_data.add_truck('Scania', truck_id=10003)


    @staticmethod
    def add_days_to_now(time1):
        time1 + timedelta(days=d)

        if self.expected_arrival_time.hour >= 20:
            remaining_hours = self.expected_arrival_time.hour - 20
            next_day_start = self.expected_arrival_time.replace(hour=6) + timedelta(days=1)
            self.expected_arrival_time = next_day_start + timedelta(hours=remaining_hours)





        # responses = []
        # for pkg_id in self.package_ids:
        #     try:
        #         self.app_data.add_package_to_route(pkg_id, self.route_id)
        #         responses.append(f"Package {pkg_id} assigned to route {self.route_id}.")
        #     except ValueError as e:
        #         responses.append(str(e))
        # return "\n".join(responses)

    #В единя случай имаме конкретн пратка, а която търсим път. В другия ще итерираме пратките на деня и ще създаваме път