
class Customer:

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        self.packages = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or value == '':
            raise ValueError('Name is invalid')
        self._name = value

    @property
    def phone_number(self):
        return self._phone_number

    # @phone_number.setter
    # def phone_number(self, value):
    #     try:
    #         number_value = int(value)
    #         self._phone_number = number_value
    #     except ValueError:
    #         raise ValueError('Phone number is invalid')


    def add_package(self):
        pass
        """ Да добавим пратката в листа с пратки на този човек + някаква допълнителна проверка"""
