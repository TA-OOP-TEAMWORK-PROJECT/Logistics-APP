### Class AppData
### methods  - search_for_route, assign_free_truck, assign_delivery_package,

from models.customer import Customer


class ApplicationData:

    def __init__(self):
        self.customer_list = Customer()

    def find_customer(self, number):
        for customer in self.customer_list:
            if customer.phone_number == number:
                return customer
        return False

    def create_customer(self, name, number):
        if self.find_customer(number):
            raise ValueError('Customer with that number already exists!')
        new_customer = Customer(name, number)
        self.customer_list.append(new_customer)