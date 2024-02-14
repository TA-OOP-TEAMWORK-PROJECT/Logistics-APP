from datetime import timedelta
from models.package import Package
from models.route import Route
from models.customer import Customer
from models.actros import Actros
from models.man import Man
from models.scania import Scania

class ApplicationData:
    def __init__(self):
        self.daily_packages = []
        self._routes = []
        self._customers = []
        self._trucks = []

    @property
    def packages(self):
        return tuple(self.daily_packages)

    @property
    def routes(self):
        return tuple(self._routes)
    
    @property 
    def customers(self):
        return tuple(self._customers)

    @property
    def trucks(self):
        return self._trucks


    def create_customer(self, name, phone_number):
        customer = Customer(name, phone_number)
        self._customers.append(customer)

    def find_customer(self, number):
        for customer in self._customers:
            if customer.phone_number == number:
                return customer
        return None

    def find_package(self, package_id):
        for pkg in self.daily_packages:
            if pkg.id == package_id:
                return pkg
        return None

    def find_route(self, route_id):
        for rt in self._routes:
            if rt.route_id == route_id:
                return rt
        return None

    def show_package_by_start_end_location(self, start, end):
        for package in self.daily_packages:
            if package.start_location == start and package.end_location == end:
                return package

    def show_route_by_start_end_location(self, start, end):
        for route in self._routes:
            if route.start_location == start and route.end_location == end:
                return route

    @staticmethod
    def calculate_eta(distance):
        average_speed_kmh = 87
        travel_time = distance / average_speed_kmh
        if travel_time > 14:
            days = travel_time//14
            hours = travel_time - (days * 14)
            travel_time = timedelta(days=days,hours=hours)
        return travel_time

    @staticmethod
    def calculate_time(current_time, travel_time):
        time = current_time + travel_time

    def create_package(self, start_location, end_location, weight, customer):
        
        if not customer:
            raise ValueError("Customer not found.")
        package = Package(start_location, end_location, weight, customer)
        self.daily_packages.append(package)
        return package

    def create_route(self, start_location, end_location):
        route = Route(start_location, end_location)
        self._routes.append(route)
        return route

    def assign_truck(self, distance, load):
        if (0 <= distance <= 8000) and ( 0 <= load <= 42000):
            truck = Scania()
            # return self.app_data.add_truck('Scania', truck_id=10001)

        elif (0 <= distance <= 10000) and (0 <= load <= 37000):
            truck = Man()
            # return self.app_data.add_truck('Scania', truck_id=10002)

        elif (0 <= distance <= 13000) and (0 <= load <= 26000):
            truck = Actros()
            # return self.app_data.add_truck('Scania', truck_id=10003)
        else:
            return ValueError("Unknown truck type.")
        self._trucks.append(truck)
        return truck


    def view_unassigned_packages(self):
        unassigned_packages = []
        for pkg in self.daily_packages:
            if not pkg.route:
                unassigned_packages.append(pkg)
        return unassigned_packages

    def view_routes_in_progress(self):
        routes_in_progress = []
        for route in self._routes:
            if route.is_in_progress():
                routes_in_progress.append(route)
        return routes_in_progress


    # update_route(),show_routes(), show_packages()
    # def add_truck(self, truck_type):
    #     if truck_type == "Actros":
    #         truck = Actros()
    #     elif truck_type == "Man":
    #         truck = Man()
    #     elif truck_type == "Scania":
    #         truck = Scania()
    #     else:
    #         raise ValueError("Unknown truck type.")
    #     self._trucks.append(truck)
    #     return truck
