from core.application_data import ApplicationData
from errors.invalid_command import InvalidCommand
from commands.create_customer import CreateCustomerCommand
from commands.create_package import CreatePackageCommand
from commands.create_delivery_route import CreateDeliveryRouteCommand
from commands.search_route import SearchRouteCommand
from commands.view_package import ViewPackagesCommand
from commands.view_package_info_by_id import ViewPackageInfoByIdCommand
from commands.view_route import ViewRouteCommand
from commands.view_route_in_progress import ViewRoutesInProgressCommand
from commands.view_unassigned_packages import ViewUnassignedPackagesCommand
from commands.assign_package_to_route import AssignPackageToRouteCommand
from commands.bulk_assign_packages_to_route import BulkAssignPackagesToRouteCommand


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data


    def create(self, input_line: str):
        cmd_name, *params = input_line.split()

        if cmd_name.lower() == 'createcustomer':
            return CreateCustomerCommand(params, self._app_data)
        if cmd_name.lower() == "createpackage":
            return CreatePackageCommand(params, self._app_data)
        if cmd_name.lower() == "assignpackagetoroute":
            return AssignPackageToRouteCommand(params, self._app_data)
        if cmd_name.lower() == "bulkassignpackagestoroute":
            return BulkAssignPackagesToRouteCommand(params, self._app_data)
        if cmd_name.lower() == "createdeliveryroute":
            return CreateDeliveryRouteCommand(params, self._app_data)
        if cmd_name.lower() == "viewpackage":
            return ViewPackagesCommand(params, self._app_data)
        if cmd_name.lower() == "searchroute":
            return SearchRouteCommand(params, self._app_data)
        if cmd_name.lower() == "viewpackageinfobyid":
            return ViewPackageInfoByIdCommand(params, self._app_data)
        if cmd_name.lower() == "viewroute":
            return ViewRouteCommand(params, self._app_data)
        if cmd_name.lower() == "viewrouteinprogress":
            return ViewRoutesInProgressCommand(params, self._app_data)
        if cmd_name.lower() == "viewunassignedpackages":
            return ViewUnassignedPackagesCommand(self._app_data)

        raise InvalidCommand(cmd_name)
