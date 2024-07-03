
class Vehicles:
    def __init__(self, mark, model):
        self.__mark = mark
        self.__model = model

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model


class Cars(Vehicles):
    def __init__(self, mark, model, year, car_type, price, seats, distance):
        super().__init__(mark, model)
        self.__year = year
        self.__car_type = car_type
        self.__price = price
        self.__seats = seats
        self.__distance = distance

    def __str__(self):
        return (f'''Марка: {self.mark}; Модель: {self.model}; Год производства: {self.year} г.; Цена: {self.price}₼; Тип: {self.car_type}; Пробег: {self.distance} км.; Мест: {self.seats}''')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year > 1990:
            self.__year = year

    @property
    def car_type(self):
        return self.__car_type

    @car_type.setter
    def car_type(self, car_type):
        self.__car_type = car_type

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, seats):
        if seats >= 2:
            self.__seats = seats

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        if value >= 0:
            self.__distance = value


class Motorcycles(Vehicles):
    def __init__(self, mark, model, year, price, distance):
        super().__init__(mark, model)
        self.__year = year
        self.__price = price
        self.__distance = distance

    def __str__(self):
        return f'''Марка: {self.mark}; Модель: {self.model}; Год производства: {self.year} г.; Цена: {self.price}₼; Пробег: {self.distance} км.'''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year > 1990:
            self.__year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance):
        if distance >= 0:
            self.__distance = distance

