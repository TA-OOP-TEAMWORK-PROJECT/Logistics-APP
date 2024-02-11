from validation_helpers import validate_params_count
from core.application_data import ApplicationData


class AssignPackageToRouteCommand:       #Use case 1
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2)
        self.package_id, self.route_id = params #не може да са инт
        self.app_data = app_data

    def execute(self):

        possible_route = self.app_data.find_route(self.route_id)
        package = self.app_data.find_package(self.package_id)
        if possible_route and package:
            # load = self.load_checker(possible_route, package)
            try:
                load = self.check_destination_load(possible_route, package)
                possible_route.load += load
                possible_route.packages.append(package) # Да се намрави функция, която маха товар при крайна дестинация
                return f"Package {self.package_id} assigned to route {self.route_id}."
            except:
                raise ValueError('No free space to load the package!')


    def check_destination_load(self, possible_route, package): #да проследя до къде сме стигнали
        #пресмятам товара от началото, като на всяка локация, на която се разтоварва изваждам товара.
        #Така до края на пътя, за който е сегашната пратка имам знание дали ще мога да я кача или не.
        pak = []
        end_loc = []
        some_destination_load = package.weight
        for k,v in possible_route.route.items():  #Преминавам през пътя
            if k == package.end_location:         # Проверявам дали това е спирката, на която трябва да се разтовари евентуално пратката
                break
            for i in possible_route.packages:     # Преминавам през пратките, които са асайнати на този път
                if k == i.start_location:         #Ако града, в който сме в момента е техният старт град, я товаря
                    pak.append(i)                  #добарям пратката като натоварена
                    some_destination_load += i.weight  #Пресмятам килограмите
                    end_loc.append(i.end_location)
                for end in range(len(pak)):            #ПРоверявам дали случайно не сме в град, в който пратка трябва да се свали
                    if k == pak[end].end_location:      #Ако да я изваждам
                        some_destination_load -= pak[end].weight

        if some_destination_load <= (possible_route.assigned_truck.capacity_kg - some_destination_load):
            return some_destination_load
        raise ValueError ('Not enough free space')


        # start_index = 0
        # end_index = 0
        # cnt = 0 #итерация през часовеъте и като се свалят килограмите, има място
        # for p in range(len(possible_route.packages)):
        #     if possible_route[p].start_location or possible_route[p].end_location == package.start_location:
        #         start_index = p
        #     if possible_route[p].end_location or possible_route[p].start_location == package.end_location:
        #         end_index = p
        #
        # return sum([pak.weight for pak in possible_route.packages[start_index:end_index+1]])


def calculate_route_distance(self):
    locations_sequence = [self.start_location] + [stop['location'] for stop in self.stops] + [self.end_location]
    return self.distances.calculate_total_route_distance(locations_sequence)



