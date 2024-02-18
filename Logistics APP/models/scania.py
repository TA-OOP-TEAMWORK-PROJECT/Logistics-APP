from models.truck import Truck
from generate_id.id_generator import TruckIdGenerator
from models.truck_status import TruckStatus


class Scania(Truck):
    scania_id_generator = TruckIdGenerator(1001, 1010)
    truck_brand = "Scania"
    capacity_kg = 42000
    max_range_km = 8000

    # трябва да се генерира, не да го задаваме ние
    def __init__(self):
        truck_id = Scania.scania_id_generator.get_id()
        super().__init__(truck_id, Scania.truck_brand,
                         Scania.capacity_kg, Scania.max_range_km)

    def release(self):
        self.status = TruckStatus.FREE
        self.scania_id_generator.used_ids.remove(self.truck_id)
        self.current_route = None
        self.current_load_kg = 0