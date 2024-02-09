### Class AppData
### methods  - search_for_route, assign_free_truck, assign_delivery_package,

from models.package import Package
from models.route import Route
from models.customer import Customer
from models.truck import Truck
from models.actros import Actros
from models.man import Man
from models.scania import Scania

class ApplicationData:
    def __init__(self):
        self._packages = []
        self._routes = []
        self._customers = []
        self._trucks = []

    @property
    def packages(self):
        return tuple(self._packages)

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

    def create_package(self, start_location, end_location, weight, customer):
        customer = self.find_customer(customer)
        if not customer:
            raise ValueError("Customer not found.")
        package = Package(start_location, end_location, weight, customer)
        self._packages.append(package)
        return package

    def create_route(self, start_location, end_location, departure_time):
        route = Route(start_location, end_location, departure_time)
        self._routes.append(route)
        return route

    # update_route(),show_routes(), show_packages()
        
    def show_package_by_start_end_location(self, start, end):
        for package in self._packages:
            if package.start_location == start and package.end_location == end:
                return package
    
    def show_route_by_start_end_location(self, start, end):
        for route in self._routes:
            if route.start_location == start and route.end_location == end:
                return route

    def add_package_to_route(self, package_id, route_id):
        package = None
        for pkg in self._packages:
            if pkg.id == package_id:
                package = pkg
                break

        route = None
        for rt in self._routes:
            if rt.route_id == route_id:
                route = rt
                break

        if not package or not route:
            raise ValueError("Package or Route not found.")

        route.add_package(package)

    def add_truck(self, truck_type, truck_id):
        if truck_type == "Actros":
            truck = Actros(truck_id)
        elif truck_type == "Man":
            truck = Man(truck_id)
        elif truck_type == "Scania":
            truck = Scania(truck_id)
        else:
            raise ValueError("Unknown truck type.")
        self._trucks.append(truck)
        return truck

    def search_for_route(self, start_location, end_location):
        for route in self._routes:
            if route.start_location == start_location and route.end_location == end_location:
                return route
        return None

    def view_unassigned_packages(self):
        unassigned_packages = []
        for pkg in self._packages:
            if not pkg.route:
                unassigned_packages.append(pkg)
        return unassigned_packages

    def view_routes_in_progress(self):
        routes_in_progress = []
        for route in self._routes:
            if route.is_in_progress():
                routes_in_progress.append(route)
        return routes_in_progress
