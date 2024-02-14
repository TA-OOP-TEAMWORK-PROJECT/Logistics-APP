import os
from models.location import Location
from generate_id.id_generator import PackageIdGenerator

class Package:


    def __init__(self, start_location, end_location, weight, customer):
        self.id = PackageIdGenerator.generate_next_package_id()
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self.customer = customer   #for customer information
        self.route = None    # classROUTE
        self.status = None
        self.daily_storage = []
        self.save_to_file()


    @property
    def start_location(self):
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        if value not in Location.possible_locations:
            raise ValueError('Invalid location!')
        self._start_location = value

    @property
    def end_location(self):
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        if value not in Location.possible_locations:
            raise ValueError('Invalid location!')
        self._end_location = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if not 0 < value <= 42000:
            raise ValueError('Package can not be less or equal to 0!') #!!!!
        self._weight = value

    def info(self):
        return (f"Package ID: {self.id}, Start Location: {self._start_location}, "
                f"End Location: {self._end_location}, Weight: {self._weight:.2f}, "
                f"Customer: {self.customer.name if self.customer else 'Package is not yet assigned'}, Assigned Route: {self.route.route_id if self.route else 'None'}")



    def __str__(self):
        pass

    def save_to_file(self):
        package_info = {
            'id': self.id,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'weight': self.weight,
            'customer': self.customer.name if self.customer else None,
            'route': self.route.route_id if self.route else None
        }

        directory_path = 'packages_info'
        file_path = os.path.join(directory_path, 'packages_info.txt')

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file_path, 'a') as file:
            file.write(str(package_info) + '\n')