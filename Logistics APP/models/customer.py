
class Customer:

    def __init__(self, name, phone_number):
        self._name = name
        self.phone_number = phone_number
        self.packages = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or value == '':
            raise ValueError('Name is invalid')
        self._name = value

    def add_package(self):
        pass
        """ Да добавим пратката в листа с пратки на този човек + някаква допълнителна проверка"""
