from models.truck import Truck
from generate_id.id_generator import TruckIdGenerator
from models.truck_status import TruckStatus


class Man(Truck):
    man_id_generator = TruckIdGenerator(1011, 1025)
    truck_brand = "Man"
    capacity_kg = 37000
    max_range_km = 10000

    def __init__(self):
        truck_id = Man.man_id_generator.get_id()
        super().__init__(truck_id, Man.truck_brand,
                         Man.capacity_kg, Man.max_range_km)


    def release(self):
        self.status = TruckStatus.FREE
        self.man_id_generator.used_ids.remove(self.truck_id)
        self.current_route = None
        self.current_load_kg = 0
