from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class ViewPackageInfoByIdCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(list(params), 1, 'ViewPackageInfoByIdCommand')
        self.package_id = params[0]
        self.app_data = app_data

    def execute(self):
        daily_package = self.app_data.find_package(self.package_id)
        package_on_route = self.app_data.find_in_progress_package(self.package_id)

        if daily_package or package_on_route:
            return package_on_route.info() if package_on_route else daily_package.info()
        else:
            return f"No package found with ID {self.package_id}"

