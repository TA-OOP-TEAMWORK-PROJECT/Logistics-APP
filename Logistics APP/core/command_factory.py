from core.application_data import ApplicationData
from errors.invalid_command import InvalidCommand
from commands.view_package import view
from commands.create_customer import CreateCustomerCommand

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data


    def create(self, input_line: str):
        cmd_name, *params = input_line.split()

        if cmd_name.lower() == 'createcustomer':
            return CreateCustomerCommand(*params, app_data=self._app_data)
        # if cmd_name.lower() == "createpackage":
        #     return CreatePackageCommand(params, self._app_data)
        # if cmd_name.lower() == "createroute":
        #     return CreateRouteCommand(params, self._app_data)
        # if cmd_name.lower() == "searchroute":
        #     return SearchRouteCommand(params, self._app_data)
        # if cmd_name.lower() == "updateroute":
        #     return UpdateRouteCommand(params, self._app_data)
        # if cmd_name.lower() == "showroutes":
        #     return ShowRoutesCommand(params, self._app_data)
        # if cmd_name.lower() == "showpackages":
        #     return ShowPackagesCommand(params, self._app_data)
        # if cmd_name.lower() == "showtrucks":
        #     return ShowTrucksCommand(params, self._app_data)

        raise InvalidCommand({cmd_name})