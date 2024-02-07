from truck import Truck


class Actros(Truck):
    vehicle_ids = tuple(range(1026, 1041))
    truck_brand = "Actros"
    capacity_kg = 26000
    max_range_km = 13000

    def __init__(self, truck_id):
        if truck_id not in Actros.vehicle_ids:
            raise ValueError(f"Truck ID {truck_id} is not valid for Actros trucks!")
        super().__init__(truck_id, truck_brand=Actros.truck_brand,
                         capacity_kg=Actros.capacity_kg, max_range_km=Actros.max_range_km)

