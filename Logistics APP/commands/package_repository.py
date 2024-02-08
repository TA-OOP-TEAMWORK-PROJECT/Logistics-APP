from models.customer import Customer
from models.distances import CitiesDistances
from models.package import Package
from sys import maxsize


class PackageRepository:


    def __init__(self, city_dist: CitiesDistances):
        customer = Customer('Goshe', '359899403020')
        self.daily_storage = [Package("ADL", "MEL", 150, customer),Package("ADL", "MEL", 150, customer), Package("BRI", "MEL", 15, customer), Package("ADL", "MEL", 150, customer)]
        self.distance_repp = city_dist


    def sum_daily_storage_weight(self):

        return sum([i.weight for i in self.daily_storage])


    def get_start_location_route(self):
        start_locations = []

        for l in self.daily_storage:
            if l not in start_locations:
                start_locations.append(l.start_location)
        return start_locations

    def current_route(self, start_city):
        route_dict = {}
        for k in self.distance_repp.distances.keys():
            if k == start_city:
                route_dict = self.distance_repp.distances[k]

        return route_dict

    def get_ordered_start_location(self):
        start_locations = self.get_start_location_route()
        route = self.current_route(start_locations[0])
        end_city = self.get_last_city()

        route_start = []
        for key in route.keys():
            for l in start_locations:
                if key == l:
                    route_start.append(l)
                    break

        route_start.append(end_city)
        return route_start


    def assign_route_to_package(self):
        pass

    def get_last_city(self):
        start_city = self.daily_storage[0].start_location
        max_distance = self.distance_repp.get_distance(start_city, self.daily_storage[0].end_location)
        end_city = self.daily_storage[0].end_location

        for i in range(1, len(self.daily_storage)):
            farthest_location = self.distance_repp.get_distance(start_city, self.daily_storage[i].end_location)

            if farthest_location >= max_distance:
                max_distance = farthest_location
                end_city = self.daily_storage[i].end_location

        return end_city


    def route_calculations(self):

        route_map = self.current_route(self.daily_storage[0].start_location)

        map = [self.daily_storage[0].start_location]
        passed_cities = ["x"] * (len(self.daily_storage) * 2)

        while True:
            for k in route_map.keys():
                for i in range(len(self.daily_storage)):
                    if self.daily_storage[i].start_location







    # rep = PackageRepository(CitiesDistances())
    # rep.order_packager_by_start_location()

    def assign_route_to_package(self):
        start_city = self.daily_storage[0].start_location
        city_order = [start_city]
        current_packages_order = []
        index = 0
        while True:  # докато не се изпразни листа с пратките

            min_distance = maxsize  # За да знам, с коя най-близка локация да продължа(старт на друга пратка, който е най- близо)
            starting_location = self.daily_storage[
                index].start_location  # start локацията, с която започваме - първата пратка!

            # същевременно гледам и за най-далечната end локация
            farthest_location = self.distance_repp.get_distance(starting_location, self.daily_storage[0].end_location)
            passed_end_locations = [self.daily_storage[0].end_location]

            index += 1
            if index == len(self.daily_storage):
                current_packages_order.append(last_delivery_package)
                break

            for package in range(index, len(self.daily_storage)):

                second_city_start_loc = self.daily_storage[package].start_location
                distance_start_locations = self.distance_repp.get_distance(starting_location, second_city_start_loc)
                last_location = self.distance_repp.get_distance(start_city, self.daily_storage[package].end_location)
                passed_loc = self.search_passed_locations(distance_start_locations, starting_location)

                if distance_start_locations <= min_distance:
                    min_distance = distance_start_locations
                    next_closest_start = self.daily_storage[package]

                if last_location > farthest_location:
                    farthest_location = last_location
                    end_city = self.daily_storage[
                        package].end_location  # или пакета дори и да го има втори път или да имам паралелно друг списък
                    # в който пазя градовете?

            current_packages_order.append(next_closest_start)
            city_order.append(next_closest_start.start_location)

            else:
            # current_packages_order.append(self.daily_storage[0]) Може би не трябва, защото в последната итерация, ще е останал само един елемент
            # който ще преценява дистанция до себе си, демек 0 и ще се добави

            current_packages_order.append(end_city)
        self.daily_storage.remove(next_closest_start)  # Като махне последния елемент ще се спре и while цикъла

        def search_passed_locations(self, distance):
            passed_locations = ["BRI", "ADL"]

            for i in passed_locations:
                distance_pass = self.distance_repp.get_distance(starting_location, passed_locations[i])

# pak = PackageRepository()
# pak.sum_daily_storage_distance()
#
# def get_dict_with_locations:
#      distance = CitiesDistances()
#             distance_dict = distance.distances
#             route_dict = {}
#             locations_during_first_distance = []
#
#
#
