"Will put test input here"

"""
createcustomer Pesho 359888010101
createcustomer Vanko 359888010102
createpackage Sydney Adelaide 50 359888010101
createpackage Melbourne Adelaide 50 359888010102
createdeliveryroute Sydney Darwin
Melbourne
Adelaide
Brisbane
AliceSprings
Perth
end
bulkassignpackagestoroute Route00001 Pkg00001 Pkg00002
createpackage Sydney Adelaide 50 359888010102
assignpackagetoroute Route00001 Pkg00003
viewroute Sydney Adelaide
viewrouteinprogress
exit

"""

# app_data = ApplicationData()
#
#
# customer1 = Customer('Pesho', '359888010101')
# customer2 = Customer('Vanko', '359888010102')
# app_data.create_customer(customer1.name, customer1.phone_number)
# app_data.create_customer(customer2.name, customer2.phone_number)
#
#
# package1 = app_data.create_package('Brisbane', 'Sydney', 10000, customer1)  # Weight that requires a specific truck type
# package2 = app_data.create_package('Melbourne', 'Adelaide', 20000, customer2)  # Another weight
#
#
# total_distance = 5000
# total_load = package1.weight + package2.weight
#
#
# route_command = CreateDeliveryRouteCommand(['Sydney', 'Adelaide'], app_data)
# route_command.execute()
#
#
# latest_route = max(app_data._routes, key=lambda x: x.route_id)
#
# latest_route.expected_arrival_time = datetime.now() - timedelta(days=1)
#
# assigned_truck = app_data.assign_truck(total_distance, total_load)
#
# latest_route.assigned_truck = assigned_truck
#
# app_data.assign_package_to_route(package1.id, latest_route.route_id)
# app_data.assign_package_to_route(package2.id, latest_route.route_id)
#
# app_data.completed_routes()
#
# v = ViewPackageInfoByIdCommand([package1.id], app_data)
# print(v.execute())
# vv = ViewPackageInfoByIdCommand([package2.id], app_data)
# print(vv.execute())
#
# delivered_package_ids = app_data.delivered_packages()
# if delivered_package_ids:
#     print(f"Delivered packages: {', '.join(delivered_package_ids)}")
# else:
#     print("No packages delivered.")