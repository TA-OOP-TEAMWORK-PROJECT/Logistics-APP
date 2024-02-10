from core.application_data import ApplicationData
from models.package import Package


class ViewUnassignedPackagesCommand:            #Use case 4 
    def __init__(self, app_data: ApplicationData):
        self.app_data = app_data

    def execute(self):
        unassigned_packages = [pkg.info() for pkg in self.app_data.daily_packages if not pkg.route]
        return "\n".join(unassigned_packages) if unassigned_packages else "No unassigned packages."