import os
from generate_id.id_generator import PackageIdGenerator
from models.package_status import PackageStatus


class Package:

    def __init__(self, start_location, end_location, weight, customer):
        self.id = PackageIdGenerator.generate_next_package_id()
        self.start_location = start_location
        self.end_location = end_location
        self._weight = weight
        self.customer = customer   #for customer information
        self.route = None    # classROUTE
        self.status = PackageStatus.NOT_ASSIGNED
        self.save_to_file()

    @property
    def start_location(self):
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        if value not in ['Sydney', 'Melbourne', 'Adelaide', 'AliceSprings', 'Brisbane', 'Darwin', 'Perth']:
            raise ValueError('Invalid location!')
        self._start_location = value

    @property
    def end_location(self):
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        if value not in ['Sydney', 'Melbourne', 'Adelaide', 'AliceSprings', 'Brisbane', 'Darwin', 'Perth']:
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
        route_id_info = f", Assigned Route: {self.route.route_id}" if self.route else ""
        return (f"Package ID: {self.id}, Status: {self.status.value}, Start Location: {self.start_location}, "
                f"End Location: {self.end_location}, Weight: {self.weight}kg{route_id_info}")

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
