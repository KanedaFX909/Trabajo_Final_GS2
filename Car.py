from datetime import date

class Car:
    def __init__(self, brand, model, color, year, km):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__year = year
        self.__km = km
        self.__date_creation = date.today()

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def year(self):
        return self.__year

    @property
    def km(self):
        return self.__km

    @property
    def date_creation(self):
        return self.__date_creation

    @date_creation.setter
    def date_creation(self, date_creation):
        self.__date_creation = date_creation