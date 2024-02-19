from datetime import timedelta, datetime
from models.package import Package
from models.route import Route
from models.customer import Customer
from models.actros import Actros
from models.man import Man
from models.scania import Scania
from models.package_status import PackageStatus
from models.truck import Truck


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

    def find_customer(self, number_id):
        try:
            phone_number = int(number_id)
            for customer in self._customers:
                if customer.phone_number == number_id:
                    return customer
        except:
            raise ValueError('Invalid number!')

    def find_package(self, package_id):
        for pkg in self.daily_packages:
            if pkg.id == package_id:
                return pkg
        return None

    def find_in_progress_package(self, pak_id):

        for r in self._routes:
            for pk in r.packages:
                if pk.id == pak_id:
                    return pk
        return None


    def find_route(self, route_id):
        for rt in self._routes:
            if rt.route_id == route_id:
                return rt
        return None

    def show_package_by_start_end_location(self, start, end): #САмо от тези през деня
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
        days = travel_time//14
        hours = travel_time - (days * 14)
        travel_time = timedelta(days=days, hours=hours)
        return travel_time

    @staticmethod
    def calculate_time(current_time, travel_time):
        time = current_time + travel_time

    def create_package(self, start_location, end_location, weight, customer):

        package = Package(start_location, end_location, weight, customer)
        self.daily_packages.append(package)
        return package

    def create_route(self, start_location, end_location):
        route = Route(start_location, end_location)
        # self._routes.append(route)
        return route

    def assign_truck(self, distance, load):
        if distance < 13000 or load > 42000:
            raise ValueError('')
        if (0 <= distance <= 8000) and (0 <= load <= 42000) and Scania.check_availability:
            truck = Scania()
            self._trucks.append(truck)
            return truck
            # return self.app_data.add_truck('Scania', truck_id=10001)

        elif (0 <= distance <= 10000) and (0 <= load <= 37000):
            truck = Man()
            self._trucks.append(truck)
            return truck

            # return self.app_data.add_truck('Scania', truck_id=10002)

        elif (0 <= distance <= 13000) and (0 <= load <= 26000):
            truck = Actros()
            self._trucks.append(truck)
            return truck

            # return self.app_data.add_truck('Scania', truck_id=10003)
        else:
            return ValueError("Unknown truck type.")
        return truck

    def view_unassigned_packages(self): #Само daily_packages
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

    def assign_package_to_route(self, package, route):
        package.route = route
        package.status = PackageStatus.ASSIGNED_TO_ROUTE
        route.packages.append(package)

    def completed_routes(self):
        time_now = datetime.now()
        remaining_routes = []

        for route in self._routes:
            if route.expected_arrival_time >= time_now:
                route.assigned_truck.release()
                print(f"Truck {route.assigned_truck.truck_id} successfully released.")
            else:
                remaining_routes.append(route)
        self._routes = remaining_routes


    def route_progress(self):
        time_now = datetime.now()
        passed_cities = []

        for route in self._routes:
            for city, arr_time in route.route.items():
                if arr_time.day <= time_now.day:
                    passed_cities.append(city)

        return passed_cities

    def delivered_packages(self):
        delivered_package_ids = []
        for route in self._routes:
            for package in route.packages:
                for k, v in route.route.items():
                    if k == package.end_location and v.day >= datetime.now().day and not package.status == PackageStatus.DELIVERED:
                        package.status = PackageStatus.DELIVERED
        if not delivered_package_ids:
            raise ValueError('No package has reached a final destination yet!')

        return delivered_package_ids



