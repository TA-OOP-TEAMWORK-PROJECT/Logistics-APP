from company.location import Location

class Package:
    _id = 0

    def __init__(self, start_location, end_location, weight, customer):
        self._id += 1
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self.customer = customer   #for customer information
        self.route = None

    @property
    def start_location(self):
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        if value not in Location.possible_locations:
            raise ValueError('Invalid location!')
        self._start_location = value

    @property
    def end_location(self):
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        if value not in Location.possible_locations:
            raise ValueError('Invalid location!')
        self._end_location = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('Package can not be less or equal to 0!')

