class CitiesDistances:
    def __init__(self):
        self.distances = {
            "Sydney": {"Melbourne": 877, "Adelaide": 1376, "AliceSprings": 2762, "Brisbane": 909, "Darwin": 3935, "Perth": 4016},
            "Melbourne": {"Sydney": 877, "Adelaide": 725, "AliceSprings": 2255, "Brisbane": 1765, "Darwin": 3752, "Perth": 3509},
            "Adelaide": {"Melbourne": 725, "Sydney": 1376,  "AliceSprings": 1530, "Brisbane": 1927, "Darwin": 3027, "Perth": 2785},
            "AliceSprings": {"Sydney": 2762, "Melbourne": 2255, "Adelaide": 1530, "Brisbane": 2993, "Darwin": 1497, "Perth": 2481},
            "Brisbane": {"Sydney": 909, "Melbourne": 1765, "Adelaide": 1927, "AliceSprings": 2993, "Darwin": 3426, "Perth": 4311},
            "Darwin": {"Sydney": 3935, "Melbourne": 3752, "Adelaide": 3027, "AliceSprings": 1497, "Brisbane": 3426, "Perth": 4025},
            "Perth": {"Sydney": 4016, "Melbourne": 3509, "Adelaide": 2785, "AliceSprings": 2481, "Brisbane": 4311, "Darwin": 4025}
        }

    def get_distance(self, from_location, to_location):
        return self.distances[from_location][to_location]


    def calculate_total_route_distance(self, locations):
        locations_arr = list(locations.keys())
        first_location = locations_arr[0]
        ttl_distance = 0

        for i in range(1, len(locations_arr)):
            next_location = locations_arr[i]
            ttl_distance += self.get_distance(first_location, next_location)
            first_location = locations_arr[i]

        return ttl_distance
