from truck import Truck


class Scania(Truck):

    truck_brand = "Scania"
    capacity_kg = 42000
    max_range_km = 8000

    # трябва да се генерира, не да го задаваме ние
    def __init__(self, truck_id):
        if truck_id not in Scania.vehicle_ids:
            raise ValueError(f"Truck ID {truck_id} is not valid for Scania trucks!")
        super().__init__(truck_id, truck_brand=Scania.truck_brand,
                         capacity_kg=Scania.capacity_kg, max_range_km=Scania.max_range_km)
