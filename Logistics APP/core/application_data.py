### Class AppData
### methods  - search_for_route, assign_free_truck, assign_delivery_package,
from datetime import timedelta, datetime
from models.package import Package
from models.route import Route
from models.customer import Customer
from models.truck import Truck
from models.actros import Actros
from models.man import Man
from models.scania import Scania
from models.package_status import PackageStatus

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

    def find_package(self, package_id): #След като вече е проверен дали пътя е ок и е избран
        for pkg in self.daily_packages:
            if pkg.id == package_id:
                return pkg
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
    def add_departure_time():
        # Създаване на обект от тип datetime, представляващ текущата дата и час
        current_datetime = datetime.now()
        # Добавяне на един ден към текущата дата, за да получите утрешната дата
        tomorrow_date = current_datetime + timedelta(days=1)
        # Създаване на утрешния ден с час 06:00
        date_time_tommorow = datetime(tomorrow_date.month, tomorrow_date.day, 6, 0)
        return date_time_tommorow

    @staticmethod
    def calculate_eta(distance): # Времето, за което се придвижваме от 1 град до друг
        average_speed_kmh = 87
        travel_time = distance / average_speed_kmh
        if travel_time > 14:
            days = travel_time//14              # 14, защото работния ден ни е 14 часа
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
            truck_type = 'Scania'
            truck = Scania()
            # return self.app_data.add_truck('Scania', truck_id=10001)

        elif (0 <= distance <= 10000) and (0 <= load <= 37000):
            truck_type = 'Man'
            truck = Man()
            # return self.app_data.add_truck('Scania', truck_id=10002)

        elif (0 <= distance <= 13000) and (0 <= load <= 26000):
            truck_type = 'Actros'
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

    def assign_package_to_route(self, package_id, route_id):
        package = self.find_package(package_id)
        route = self.find_route(route_id)
        if package and route:
            package.route = route
            package.status = PackageStatus.ASSIGNED_TO_ROUTE
            self.route.packages.append(package)
        else:
            raise ValueError("Package not found.")

    

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

    # def search_for_route(self, start_location, end_location):
    #     for route in self._routes:
    #         if route.start_location == start_location and route.end_location == end_location:
    #             return route
    #     return None
    #

