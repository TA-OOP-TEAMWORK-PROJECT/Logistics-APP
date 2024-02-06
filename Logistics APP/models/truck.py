from truck_status import TruckStatus


class Truck:
    def __init__(self, truck_id, truck_brand, capacity_kg, max_range_km):
        self._truck_id = truck_id
        self._truck_brand = truck_brand
        self._capacity_kg = capacity_kg
        self._max_range_km = max_range_km
        self.status = TruckStatus.FREE
        self.current_route = None
        self.current_load_kg = 0

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

    def update_load(self, package_weight):
        new_load = self.current_load_kg + package_weight
        if new_load <= self.capacity_kg:
            self.current_load_kg = new_load
            if new_load == self.capacity_kg:
                self.status = TruckStatus.ON_THE_ROAD_FULL
            else:
                self.status = TruckStatus.ON_THE_ROAD_NOT_FULL
        else:
            raise ValueError("We cannot have more packages. The truck is full!")

    def assign_to_route(self, route_id):
        if self.status == TruckStatus.FREE:
            self.status = TruckStatus.ON_THE_ROAD_NOT_FULL
            self.current_route = route_id
        elif self.status == TruckStatus.ON_THE_ROAD_NOT_FULL:
            pass
        else:
            raise Exception("Truck is not available for new assignments")

    def release(self):
        self.status = TruckStatus.FREE
        self.current_route = None
        self.current_load_kg = 0
