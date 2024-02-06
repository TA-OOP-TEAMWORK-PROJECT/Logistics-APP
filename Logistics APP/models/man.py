from truck import Truck


class Man(Truck):
    vehicle_ids = tuple(range(1011, 1026))

    def __init__(self, truck_id):
        if truck_id not in Man.vehicle_ids:
            raise ValueError(f"Truck ID {truck_id} is not valid for Man trucks!")
        truck_brand = "Man"
        capacity_kg = 37000
        max_range_km = 10000
        super().__init__(truck_id, truck_brand, capacity_kg, max_range_km)