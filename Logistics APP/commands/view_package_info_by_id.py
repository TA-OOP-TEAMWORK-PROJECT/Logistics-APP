from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class ViewPackageInfoByIdCommand:        #Use Case 5
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self.package_id = params[0]
        self.app_data = app_data

    def execute(self):
        package = self.app_data.find_package(self.package_id)
        if package:
            return package.info()
        else:
            return f"No package found with ID {self.package_id}"