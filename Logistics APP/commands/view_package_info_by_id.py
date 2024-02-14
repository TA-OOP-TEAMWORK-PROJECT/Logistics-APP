from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class ViewPackageInfoByIdCommand:        #Use Case 5
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self.package_id = params[0]
        self.app_data = app_data

    def execute(self):
        package = next((p for p in self.app_data.daily_packages if p.id == self.package_id), None)
        return package.info() if package else f"No package found with ID {self.package_id}."