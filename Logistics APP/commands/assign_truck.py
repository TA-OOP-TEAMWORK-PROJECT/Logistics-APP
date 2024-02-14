from core.application_data import ApplicationData


class AssignTruck:

    def __init__(self, params, app_data: ApplicationData):

        self.distance = int(params[0])
        self.load = float(params[1])
        self.app_data = app_data

    def execute(self, distance, load):
        if (0 <= distance <= 8000) and (0 <= load <= 42000):
            truck_type = 'Scania'
            # return self.app_data.add_truck('Scania', truck_id=10001)

        elif (0 <= distance <= 10000) and (0 <= load <= 37000):
            truck_type = 'Man'
            # return self.app_data.add_truck('Scania', truck_id=10002)

        elif (0 <= distance <= 13000) and (0 <= load <= 26000):
            truck_type = 'Actros'
            # return self.app_data.add_truck('Scania', truck_id=10003)
        else:
            return 'No truck found'
        truck = self.app_data.add_truck(truck_type)

        return truck
