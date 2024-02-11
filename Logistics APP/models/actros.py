from models.truck import Truck
from generate_id.id_generator import TruckIdGenerator


class Actros(Truck):
    actros_id_generator = TruckIdGenerator(1026, 1040)
    truck_brand = "Actros"
    capacity_kg = 26000
    max_range_km = 13000

    def __init__(self):
        truck_id = Actros.actros_id_generator.get_id()
        super().__init__(truck_id, Actros.truck_brand,
                         Actros.capacity_kg, Actros.max_range_km)

