from datetime import datetime, timedelta
from generate_id.id_generator import RouteIdGenerator
from distances import CitiesDistance
from event_log import EventLog
from actros import Actros
from man import Man
from scania import Scania

class Route:
    def __init__(self, start_location, end_location, departure_time):
        route_id = RouteIdGenerator.generate_next_route_id()
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.departure_time = departure_time
        self.intermediate_stops = []
        self.expected_arrival_time = None
        self.assigned_truck = None
        self.packages = []
        self.city_distances = CitiesDistance()
        self.event_logs = []
        self.event_logs.append(EventLog(f"Route {route_id} created."))

    def set_expected_arrival_time(self, arrival_time):
        self.expected_arrival_time = arrival_time

    def calculate_route_distance(self):
        locations_sequence = [self.start_location] + [stop['location'] for stop in self.stops] + [self.end_location]
        return self.city_distances.calculate_total_route_distance(locations_sequence)

    def add_intermediate_stop(self, stop_location, expected_arrival_time):
        self.intermediate_stops.append({'location': stop_location, 'expected arrival time': expected_arrival_time})
        self.event_logs.append(EventLog(f"Stop added: {stop_location}."))

    def truck_is_compatible(self, truck):
        total_distance = self.calculate_route_distance()
        if total_distance > truck.max_range_km:
            return False
        if sum(package.weight for package in self.packages) + truck.current_load_kg > truck.capacity_kg:
            return False
        return True

    def get_truck_instance_by_id(self, truck_id):
        if truck_id in Actros.vehicle_ids:
            return Actros(truck_id)
        elif truck_id in Man.vehicle_ids:
            return Man(truck_id)
        elif truck_id in Scania.vehicle_ids:
            return Scania(truck_id)
        else:
            self.event_logs.append(
                EventLog(f"Can not assign truck with invalid ID {truck_id} to route {self.route_id}."))
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

    def add_package(self, package):
        if not self.assigned_truck:
            raise ValueError("No truck assigned to the route yet.")
        if package.weight + self.current_load() > self.assigned_truck.capacity_kg:
            raise ValueError("Adding this package would exceed the truck's capacity.")
        if package.start_location != self.start_location or package.end_location != self.end_location:
            raise ValueError("Package start or end location does not match the route.")
        self.packages.append(package)
        self.event_logs.append(EventLog(f"Package {package.id} added to route {self.route_id}."))

    def current_load(self):
        return sum(package.weight for package in self.packages)

    def calculate_eta(self):            #ETA - estimated time of arrival
        average_speed_kmh = 87
        current_time = self.departure_time
        for i, stop in enumerate(self.intermediate_stops):
            if i == 0:
                prev_location = self.start_location
            else:
                prev_location = self.intermediate_stops[i - 1]['location']
            next_location = stop['location']
            distance = self.city_distances.get_distance(prev_location, next_location)
            travel_time = timedelta(hours=distance / average_speed_kmh)

            #Тук предвиждаме някакво време, в което ще товарим и шофьора ще почива на някоя от спирките.
            stop_duration = timedelta(minutes=30)

            current_time += travel_time + stop_duration
            stop['expected_arrival_time'] = current_time

            self.event_logs.append(EventLog(f"Estimated arrival at {next_location}: {current_time}."))

        # Пресмятаме времето от последната междинна спирка до крайната спирка.
        final_leg_distance = self.city_distances.get_distance(self.intermediate_stops[-1]['location'], self.end_location)
        final_leg_travel_time = timedelta(hours=final_leg_distance / average_speed_kmh)
        self.expected_arrival_time = current_time + final_leg_travel_time

        self.event_logs.append(
            EventLog(f"Estimated arrival at final destination {self.end_location}: {self.expected_arrival_time}."))

    def info(self):
        return (f"Route ID: {self.route_id}, Start Location: {self.start_location}, "
                f"End Location: {self.end_location}, Departure Time: {self.departure_time}, "
                f"Expected Arrival Time: {self.expected_arrival_time}, "
                f"Assigned Truck: {self.assigned_truck.truck_id if self.assigned_truck else 'None'}")

    def is_in_progress(self):
        now = datetime.now()
        return self.departure_time <= now < (self.expected_arrival_time or now + timedelta(1))