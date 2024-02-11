class PackageIdGenerator:
    id_count = 0

    @classmethod
    def generate_next_package_id(cls):
        cls.id_count += 1 
        return f'Pkg{cls.id_count:05d}'

class RouteIdGenerator:
    id_count = 0

    @classmethod
    def generate_next_route_id(cls):
        cls.id_count += 1 
        return f'Route{cls.id_count:05d}'

class TruckIdGenerator:
    scania_brand_id = range(1001, 1011) # да не е повече или равно от 1011
    vehicle_ids_id = range(1011, 1026)
    actros_brand_id = range(1026, 1041)


    def __init__(self,brand):
        self.brand = brand

    def generate_truck_id(self):
        if self.brand == 'Scania':
            return TruckIdGenerator.scania_brand_id.next()
        elif self.brand == 'Man':
            pass
        elif self.brand == 'Actros':
            pass
