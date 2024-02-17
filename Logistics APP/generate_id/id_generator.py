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
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.available_ids = set(range(start, end + 1))
        self.used_ids = set()

    def get_id(self):
        if not self.available_ids:
            raise Exception("No IDs available.")
        new_id = self.available_ids.pop()
        self.used_ids.add(new_id)
        return new_id

    def reset(self):        #Използваме го само за тестовете, защото вади Exception: No IDs available., без него.
        self.available_ids = set(range(self.start, self.end + 1))
        self.used_ids = set()


