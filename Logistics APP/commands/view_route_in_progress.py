
from core.application_data import ApplicationData

class ViewRoutesInProgressCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.app_data = app_data
        self.start = params[0]
        self.end = params[1]

    def execute(self):

        suitable_routes = self.search_routes(self.app_data._routes)
        if suitable_routes:
            return self.info(suitable_routes)


    def search_routes(self, routes):
        current_routes = []
        for r in routes:
            cities = list(r.route.keys())
            if self.start in cities and self.end in cities:
                if cities.index(self.start) < cities.index(self.end):
                    current_routes.append(r)

        return routes

    def info(self, suitable_routes):
        result = ''

        for route in suitable_routes:
            for k, v in route.route.items():
                result += f' {k} ({v.strftime('%b %dth %H:%Mh')}) →'

        return result.strip('→')

