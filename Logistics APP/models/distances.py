class CitiesDistances:
    def __init__(self):
        self.distances = {
            "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
            "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
            "ADL": {"MEL": 725, "SYD": 1376,  "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
            "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
            "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
            "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
            "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025}
        }

    def get_distance(self, from_location, to_location):
        return self.distances[from_location][to_location]

    def calculate_total_route_distance(self, locations):
        ttl_distance = 0
        for i in range(len(locations) - 1):
            ttl_distance += self.get_distance(locations[i], locations[i + 1])
        return ttl_distance
