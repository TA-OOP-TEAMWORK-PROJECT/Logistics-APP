import os
from models.truck_status import TruckStatus



class Truck:
    def __init__(self, truck_id, truck_brand, capacity_kg, max_range_km):
        self._truck_id = truck_id
        self._truck_brand = truck_brand
        self._capacity_kg = capacity_kg
        self.current_load = 0
        self._max_range_km = max_range_km
        self.status = TruckStatus.FREE
        self.current_route = None
        self.save_to_file()

    @property
    def truck_id(self):
        return self._truck_id

    @property
    def truck_brand(self):
        return self._truck_brand

    @property
    def capacity_kg(self):
        return self._capacity_kg

    @property
    def max_range_km(self):
        return self._max_range_km

    #METHODS
    def check_availability(self):
        return self.status in [TruckStatus.FREE, TruckStatus.ON_THE_ROAD_NOT_FULL]

    def update_load(self, package_weight):     # when assign package
        new_load = self.current_load_kg + package_weight
        if new_load <= self.capacity_kg:
            self.current_load_kg = new_load
            if new_load == self.capacity_kg:
                self.status = TruckStatus.ON_THE_ROAD_FULL
            else:
                self.status = TruckStatus.ON_THE_ROAD_NOT_FULL
        else:
            raise ValueError("We cannot have more packages. The truck is full!")

    def assign_to_route(self, route):
        if self.check_availability():
            self.current_route = route
            self.status = TruckStatus.ON_THE_ROAD_NOT_FULL
        else:
            raise Exception("Truck is not available for new assignments")

    def release(self):
        self.status = TruckStatus.FREE
        self.current_route = None
        self.current_load_kg = 0


    def save_to_file(self):
        truck_info = {
            'truck_id': self.truck_id,
            'truck_brand': self.truck_brand,
            'capacity_kg': self.capacity_kg,
            'max_range_km': self.max_range_km,
            'status': self.status,
            'current_route': self.current_route,
            'current_load_kg': self.current_load_kg
        }

        directory_path = 'trucks_info'
        file_path = os.path.join(directory_path, 'trucks_info.txt')

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file_path, 'a') as file:
            file.write(str(truck_info) + '\n')