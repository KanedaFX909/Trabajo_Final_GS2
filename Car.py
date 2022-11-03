from datetime import date

class Car:
    def __init__(self, brand, model, color, year, km):
        #Atributos inicializados en modo privado
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__year = year
        self.__km = km
        self.__date_creation = date.today()

    @property # Acceso a la variable por medio del decorador @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand


    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model


    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color


    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year = year


    @property
    def km(self):
        return self.__km
    @property
    def date_creation(self):
        return self.__date_creation

    # Setter decorado c/ atributo de acceso global
    @date_creation.setter
    def date_creation(self, date_creation):
        self.__date_creation = date_creation