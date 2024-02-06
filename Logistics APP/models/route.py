from truck import Truck
from datetime import datetime, timedelta


class Route:
    def __init__(self, route_id, start_location, end_location, departure_time):
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.departure_time = departure_time
        self.stops = []
        self.expected_arrival_time = None
        self.assigned_truck = None
        self.packages = []

    def set_expected_arrival_time(self, arrival_time):
        self.expected_arrival_time = arrival_time

    def add_stop(self, stop_location, expected_arrival_time):
        self.stops.append({'location': stop_location, 'expected arrival time': expected_arrival_time})

    def assign_truck(self, truck):
        if truck.check_availability():
            self.assigned_truck = truck
            truck.assign_to_route(self.route_id)
        else:
            raise ValueError("Truck is not available!")

    def add_package(self, package):
        if self.assigned_truck and self.assigned_truck.current_load_jg + package.weight_kg <= self.assigned_truck.capacity_kg:
            self.packages.append(package)
            self.assigned_truck.update_load(package.weight_kg)
        else:
            raise ValueError("Package cannot be added. Truck is already full or there's no available truck!")


    def calculate_estimated_arrivals(self):
        pass

