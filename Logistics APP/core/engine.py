from datetime import datetime, timedelta

from commands.bulk_assign_packages_to_route import BulkAssignPackagesToRouteCommand
from commands.create_delivery_route import CreateDeliveryRouteCommand
from commands.view_package_info_by_id import ViewPackageInfoByIdCommand
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from errors.invalid_command import InvalidCommand
from models.customer import Customer
from models.package import Package


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


customer1 = Customer('Pesho', 359888010101)
customer2 = Customer('Vanko', 359888010102)
package1 = Package('Brisbane', 'Sydney', 50, customer1)
package2 = Package('Melbourne', 'Adelaide', 50, customer2)
app_data = ApplicationData()
create_route = CreateDeliveryRouteCommand(['Sydney', 'Adelaide'], app_data)

time_now = datetime.now()
time_tomorrow = time_now + timedelta(days=1)
route = create_route.execute()
route.route = {'Sydney': time_now, 'Adelaide': time_now}
route.packages = [package1, package2]
app_data._routes.append(route)
bulk_ass = BulkAssignPackagesToRouteCommand([package1, package2], app_data)
bulk_ass.execute()
create_route.execute()

app_data._routes.append(route)
print(app_data.delivered_packages())
v = ViewPackageInfoByIdCommand([package1.id], app_data)
vv = ViewPackageInfoByIdCommand([package2.id], app_data)
v.execute()
print(vv.execute())



# createcustomer Vanko 359888010102
# createpackage Sydney Adelaide 50 359888010101
# createpackage Melbourne Adelaide 50 359888010102
# createdeliveryroute Sydney Darwin
# Melbourne
# Adelaide
# Brisbane
# AliceSprings
# Perth
# end
# bulkassignpackagestoroute Route00001 Pkg00001 Pkg00002
# createpackage Sydney Adelaide 50 359888010102
# assignpackagetoroute Route00001 Pkg00003
# exit
