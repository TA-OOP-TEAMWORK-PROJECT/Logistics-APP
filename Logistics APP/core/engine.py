from datetime import datetime, timedelta

from commands.bulk_assign_packages_to_route import BulkAssignPackagesToRouteCommand
from commands.create_delivery_route import CreateDeliveryRouteCommand
from commands.view_package_info_by_id import ViewPackageInfoByIdCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from errors.invalid_command import InvalidCommand
from models.customer import Customer
from models.package import Package
from models.route import Route


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        output = []
        while True:
            try:
                input_line = input()

                if input_line.lower() == 'exit':
                    break

                command = self._command_factory.create(input_line)
                output.append(command.execute())
            except ValueError as err:
                output.append(err.args[0])

        print('\n'.join(output))
