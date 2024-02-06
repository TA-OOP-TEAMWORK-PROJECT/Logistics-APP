from truck import Truck


class Scania(Truck):
    vehicle_ids = tuple(range(1001, 1011))

    def __init__(self, truck_id):
        if truck_id not in Scania.vehicle_ids:
            raise ValueError(f"Truck ID {truck_id} is not valid for Scania trucks!")
        truck_brand = "Scania"
        capacity_kg = 42000
        max_range_km = 8000
        super().__init__(truck_id, truck_brand, capacity_kg, max_range_km)