class Accessories:
    def __init__(self, type_of_accessory, price):
        self.__type_of_accessory = type_of_accessory
        self.__price = price

    def __str__(self):
        return (f'''Аксессуар: {self.__type_of_accessory}; Цена: {self.__price}₼''')

    @property
    def type_of_accessory(self):
        return self.__type_of_accessory

    @type_of_accessory.setter
    def type_of_accessory(self, type_of_accessory):
        self.__type_of_accessory = type_of_accessory

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value