class PackageIdGenerator:
    id_count = 0

    @classmethod
    def generate_next_package_id(cls):
        cls.id_count += 1 
        return cls.id_count

class RouteIdGenerator:
    id_count = 0

    @classmethod
    def generate_next_route_id(cls):
        cls.id_count += 1 
        return cls.id_count