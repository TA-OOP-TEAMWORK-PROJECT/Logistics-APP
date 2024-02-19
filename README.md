# Logistics App

## Description

The Logistics App is a console application created to help a large Australian corporation entering the freight business coordinate package delivery between hubs in significant Australian cities. Workers can use it to keep track of package information, designate or find appropriate delivery routes, and keep an eye on the condition of delivery vehicles, packages, and routes.

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Navigate to the project directory.
4. You're ready to use the Logistics App!

## Usage

1. Run the application using Python.
2. Follow the prompts to perform various operations such as creating customers, delivery packages, routes, updating routes, and viewing information about routes, packages, customers and trucks.
3. Save the application state to the file system as needed.

## Usage Commands

The Logistics App supports the following commands for managing package delivery:

### Create Customer

Command: `createcustomer`

Description: Creates a new customer record in the system.

- `<customer_name>`: The name of the customer. (string)

- `<phone_number>`: The phone number of the customer. (string)

Usage: `createcustomer <customer name> <phone_number>`

Example: createcustomer 'Hugh Jackman' 061412345678

### Create Package

### Command: `createpackage`

Description: Creates a new delivery package in the system.

Usage: `createpackage <start_location> <end_location> <weight> <customer_phone_number>`

- `<start_location>`: The starting location of the delivery package. (string)

- `<end_location>`: The ending location of the delivery package. (string)

- `<weight>`: The weight of the delivery package in kilograms (kg). (float or integer)

- `<customer_phone_number>`: The phone number of the customer associated with the delivery package. (string)

Example: createpackage Sydney Melbourne 45 061412345678

### Command: `assignpackagetoroute`

Description: Assigns a package to a specific delivery route.

Usage: `assignpackagetoroute <package_id> <route_id>`

- `<package_id>`: The unique identifier of the package to be assigned to the delivery route. This should be in the format `PkgXXXXX`, where XXXXX represents the unique ID of the package. (string)

- `<route_id>`: The unique identifier of the delivery route to which the package will be assigned. This should be in the format `RouteXXXXX`, where XXXXX represents the unique ID of the route. (string)

Example: assignpackagetoroute Pkg00001 Route00001

### Command: `bulkassignpackagestoroute`

Description: Bulk assigns multiple packages to a specified delivery route.

Usage: `bulkassignpackagestoroute <route_id> <package_id_1> [<package_id_2> ... <package_id_n>]`

- `<route_id>`: The unique identifier of the delivery route to which the packages will be bulk assigned. This should be in the format `RouteXXXXX`, where XXXXX represents the unique ID of the route. (string)

- `<package_id_1> [<package_id_2> ... <package_id_n>]`: The unique identifiers of the packages to be bulk assigned to the specified delivery route. These should be in the format `PkgXXXXX`, where XXXXX represents the unique ID of each package. Users can specify multiple package IDs separated by spaces to bulk assign multiple packages at once. (string)

Example: bulkassignpackagestoroute Route00001 Pkg00001 Pkg00002 Pkg00003

### Create Delivery Route

### Command: `createdeliveryroute`

Description: Creates a new delivery route in the system.

Usage: `createdeliveryroute <start_location> <end_location> [<additional_destinations>]`

- `<start_location>`: The starting location of the delivery route. (string)

- `<end_location>`: The ending location of the delivery route. (string)

- `[<additional_destinations>]`: Optional additional destinations for the route. Users can input multiple destinations after the start and end locations. After entering all additional destinations, type 'end' to finalize the route creation. Each additional destination should be provided as a string. (string)

Example: createdeliveryroute "Sydney" "Melbourne" "Adelaide" "Brisbane" end


### Command: `viewpackage`

Description: Displays information about a specific package in the system.

Usage: `viewpackage <start_location> <end_location>`

- `<start_location>`: The starting location of the package to be viewed. (string)

- `<end_location>`: The ending location of the package to be viewed. (string)

Example: viewpackage "Sydney" "Melbourne"


### Command: `viewpackageinfobyid`

Description: Displays detailed information about a package based on its ID.

Usage: `viewpackageinfobyid <package_id>`

- `<package_id>`: The unique identifier of the package for which detailed information is to be displayed. These should be in the format `PkgXXXXX`, where XXXXX represents the unique ID of each package. (string)

Example: viewpackageinfobyid Pkg00001


### Command: `viewroute`

Description: Displays information about a specific delivery route in the system.

Usage: `viewroute <route_id>`

- `<route_id>`: The unique identifier of the delivery route to which the packages will be bulk assigned. This should be in the format `RouteXXXXX`, where XXXXX represents the unique ID of the route. (string)

Example: viewroute Route00001


### Command: `viewrouteinprogress`

Description: Displays information about delivery routes that are currently in progress.

Usage: `viewrouteinprogress`



### Command: `viewunassignedpackages`

Description: Displays a list of packages that have not yet been assigned to a delivery route.

Usage: `viewunassignedpackages`


## License

All rights reserved

## Credits

- Snezhana Petrova
- Simeon Hristov
- Nikolay Stankov


### Example input

```
createcustomer Pesho 359888010101
createcustomer Vanko 359888010102
createpackage Sydney Adelaide 50 359888010101
createpackage Melbourne Adelaide 50 359888010102
viewunassignedpackages
createdeliveryroute Sydney Darwin
Melbourne
Adelaide
Perth
end
bulkassignpackagestoroute Route00001 Pkg00001 Pkg00002
createpackage Sydney Adelaide 50 359888010102
viewpackageinfobyid Pkg00001
viewpackageinfobyid Pkg00002
assignpackagetoroute Route00001 Pkg00003
viewpackageinfobyid Pkg00003
viewroute Route00001
exit
```

### Example output

```
New customer with name Pesho and number 359888010101 created!
New customer with name Vanko and number 359888010102 created!
Package with Pkg00001 was created!
Package with Pkg00002 was created!
Package ID: Pkg00001, Status: not_assigned, Start Location: Sydney, End Location: Adelaide, Weight: 50.0kg
Package ID: Pkg00002, Status: not_assigned, Start Location: Melbourne, End Location: Adelaide, Weight: 50.0kg
Route with Route00001 was created!
Packages assigned to route with id number Route00001:
Pkg00001
Pkg00002
Package with Pkg00003 was created!
Package ID: Pkg00001, Status: assigned_to_route, Start Location: Sydney, End Location: Adelaide, Weight: 50.0kg, Assigned Route: Route00001        
Package ID: Pkg00002, Status: assigned_to_route, Start Location: Melbourne, End Location: Adelaide, Weight: 50.0kg, Assigned Route: Route00001     
Package Pkg00003 assigned to route Route00001.
Package ID: Pkg00003, Status: assigned_to_route, Start Location: Sydney, End Location: Adelaide, Weight: 50.0kg, Assigned Route: Route00001        
Route ID: Route00001, Start Location: Sydney, End Location: Darwin, Departure Time: Feb 20th 06:00h, Expected Arrival Time: Feb 25th 10:01h,  Assigned Truck: 1001
```
