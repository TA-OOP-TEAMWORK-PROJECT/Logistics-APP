### Class AppData
### methods  - search_for_route, assign_free_truck, assign_delivery_package,

from models.package import Package
from models.route import Route
from models.customer import Customer

class ApplicationData:
    def __init__(self):
        self._packages = []
        self._routes = []
        self._customers = []
    


    @property
    def packages(self):
        return tuple(self._packages)
    
    @property 
    def customers(self):
        return tuple(self._customers)
    
    def create_customer(self, name, phone_number):
        customer = Customer(name, phone_number)
        self._customers.append(customer)

    def find_customer(self, number):
        for customer in self._customers:
            if customer.phone_number == number:
                return True
        return False
    

    def create_package(self, start_location, end_location, weight):
        package = Package(start_location, end_location, weight)
        self._packages.append(package)

    def create_route(self, start_location, end_location, departure_time, arrival_time):
        route = Route(start_location, end_location, departure_time, arrival_time)
        self._route.append(route)

    # update_route(),show_routes(), show_packages()
        
    def show_package_by_start_endlocation(self, start, end):
        for package in self._packages:
            if package.start_location == start and package.end_location == end:
                return package
    
    def show_route_by_start_end_location(self, start, end):
        for route in self._routes:
            if route.start_location == start and route.end_location == end:
                return route