import os
from datetime import datetime, timedelta
from generate_id.id_generator import RouteIdGenerator
from models.distances import CitiesDistances
from models.event_log import EventLog
from models.actros import Actros
from models.man import Man
from models.scania import Scania
from commands.validation_helpers import parse_departure_time
# from core.application_data import ApplicationData

class Route:
    def __init__(self, start_location, end_location, customer):
        route_id = RouteIdGenerator.generate_next_route_id()
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.departure_time = parse_departure_time()
        self.expected_arrival_time = None
        self.assigned_truck = None
        self.route = {}     #start_location: self.departure_time, end_location:self.expected_arrival_time
        self.packages = [] #tuple?
        self.distances = CitiesDistances()
        self.save_to_file()

    @property
    def load(self):  # не е current, защото се иска за целия път
        return sum(package.weight for package in self.packages)

    # def calculate_location_distance(self, first_location, second_location):
    #     return self.distance.get_distance(first_location, second_location)

    # def add_intermediate_stop(self, stop_location, expected_arrival_time):
    #     self.intermediate_stops.append({'location': stop_location, 'expected arrival time': expected_arrival_time})
    #     self.event_logs.append(EventLog(f"Stop added: {stop_location}."))

    def add_package(self, package):
        if not self.assigned_truck:
            raise ValueError("No truck assigned to the route yet.")
        if package.weight + self.current_load() > self.assigned_truck.capacity_kg:
            raise ValueError("Adding this package would exceed the truck's capacity.")
        if package.start_location != self.start_location or package.end_location != self.end_location:
            raise ValueError("Package start or end location does not match the route.")
        self.packages.append(package)

    def calculate_route_distance(self):
        locations_sequence = [self.start_location] + [stop['location'] for stop in self.stops] + [self.end_location]
        return self.distances.calculate_total_route_distance(locations_sequence)

    def truck_is_compatible(self, truck):
        total_distance = self.calculate_route_distance()
        if total_distance > truck.max_range_km:
            return False
        if sum(package.weight for package in self.packages) + truck.current_load_kg > truck.capacity_kg:
            return False
        return True


    def get_truck_instance_by_id(self, truck_id):
        if truck_id in Actros.actros_id_generator:
            return Actros(truck_id)
        elif truck_id in Man.man_id_generator:
            return Man(truck_id)
        elif truck_id in Scania.scania_id_generator:
            return Scania(truck_id)
        else:
            raise ValueError(f"Truck ID {truck_id} is not valid !")

    def assign_truck(self, truck):
        if truck.check_availability() and self.truck_is_compatible(truck):
            self.assigned_truck = truck
            truck.assign_to_route(self.route_id)
            self.event_logs.append(EventLog(f"Truck {truck.truck_id} assigned to route {self.route_id}."))
        else:
            self.event_logs.append(
                EventLog(f"Truck {truck.truck_id} is not available or not compatible with the route requirements."))
            raise ValueError(f"Truck {truck.truck_id} is not available or not compatible with the route requirements.")


    @staticmethod
    def add_departure_time():
        # Създаване на обект от тип datetime, представляващ текущата дата и час
        current_datetime = datetime.now()
        # Добавяне на един ден към текущата дата, за да получите утрешната дата
        tomorrow_date = current_datetime + timedelta(days=1)
        # Създаване на утрешния ден с час 06:00
        date_time_tommorow = datetime(tomorrow_date.month, tomorrow_date.day, 6, 0)
        return date_time_tommorow

    # def calculate_eta(self):            #ETA - estimated time of arrival
    #     average_speed_kmh = 87
    #     current_time = self.departure_time
    #     for i, stop in enumerate(self.route):
    #         if i == 0:
    #             prev_location = self.start_location
    #         else:
    #             prev_location = self.route[i - 1]['location']
    #         next_location = stop['location']
    #         distance = self.distances.get_distance(prev_location, next_location)
    #         travel_time = timedelta(hours=distance / average_speed_kmh)
    #
    #         self.event_logs.append(EventLog(f"Estimated arrival at {next_location}: {current_time}."))

        # Пресмятаме времето от последната междинна спирка до крайната спирка.
        # final_leg_distance = self.distances.get_distance(self.route[-1]['location'], self.end_location)
        # final_leg_travel_time = timedelta(hours=final_leg_distance / average_speed_kmh)
        # self.expected_arrival_time = current_time + final_leg_travel_time
        #
        # self.event_logs.append(
        #     EventLog(f"Estimated arrival at final destination {self.end_location}: {self.expected_arrival_time}."))

    def info(self):
        return (f"Route ID: {self.route_id}, Start Location: {self.start_location}, "
                f"End Location: {self.end_location}, Departure Time: {self.departure_time}, "
                f"Expected Arrival Time: {self.expected_arrival_time}, "
                f"Assigned Truck: {self.assigned_truck.truck_id if self.assigned_truck else 'None'}")
# f"{Sydney} (Oct 12th 06:00h) → Melbourne (Oct 12th 20:00h) → Adelaide (Oct 13th 15:00h)

    def is_in_progress(self):
        now = datetime.now()
        return self.departure_time <= now < (self.expected_arrival_time or now + timedelta(1))

#         self.event_logs = []
#         self.event_logs.append(EventLog(f"Route {route_id} created."))


    # def add_to_route(self, package):
    #     #search start - end_location
    #
    #
    #     dist = self.distances.get_distance(self.start_location, package.start_location)
    #     dist = self.distances.get_distance(self.start_location, package.end_location)
    #
    #     total_weight = 0
    #     for i in self.packages:
    #         total_weight += i.weight
    #
    #     if total_weight <= max_weight:
    #         self.packages.append(package)
    #
    #     self.route.append(start,end loca)# or insert
    #
    #     def set_expected_arrival_time(self, arrival_time):
    #         self.expected_arrival_time = arrival_time

    def save_to_file(self):
        route_info = {
            'route_id': self.route_id,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'departure_time': self.departure_time,
            'expected_arrival_time': self.expected_arrival_time,
            'assigned_truck': self.assigned_truck.truck_id if self.assigned_truck else None
        }

        directory_path = 'routes_info'
        file_path = os.path.join(directory_path, 'routes_info.txt')

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file_path, 'a') as file:
            file.write(str(route_info) + '\n')