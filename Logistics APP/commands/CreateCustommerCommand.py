class CreateCustomer:

    def __init__(self, *params, app_data):
        self.validate_params_count(params, 2)
        self.params = params
        self.app_data = app_data  #ApplicationData

    def execute(self):  #да имаме списък с customers който търси по телефонен номер???!!!!Или номер на пратка и номер на клиент да са едни и същи като в workshop 3
        name, number = self.params
        if self.app_data.find_customer:
            raise ValueError('Customer with that number already exists!')

        self.app_data.create_customer(name, number)
        return f'New customer with {name} and {number} created!'

    def validate_params_count(self,params, count):
        if len(params) != count:
            raise ValueError(
                f'Invalid number of arguments. Expected: {count}; received: {len(params)}.")')
