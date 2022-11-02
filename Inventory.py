class Inventory:
    def __init__(self, vehicles=None):
        self.__vehicles = vehicles

    def add_car(self, car):
        self.__vehicles.append(car)
        return "Car added"

    def delete_car(self, car_id):
        try:
            del self.__vehicles[car_id]   
        except IndexError:
            return "El ID no existe"
        else:
            return "Auto eliminado exitosamente"

    def get_vehicles(self):
        return self.__vehicles

    @staticmethod
    def convert_to_save_literal(vehicles):

        return'\n'.join(
            f"{car.brand}\t{car.model}\t{car.color}\t{car.year}\t{car.km}\t{car.date_creation}"
        for car in vehicles)

    @staticmethod
    def convert_to_literal(vehicles):
        car_list = "Marca\tModelo\tColor\tAño\tKM\tFecha de creación\n\n"
        car_list += '\n'.join(
            f"{car.brand}\t{car.model}\t{car.color}\t{car.year}\t{car.km}\t{car.date_creation}"
        for car in vehicles)
        return car_list

    @staticmethod
    def convert_to_literal_indexed(vehicles):
        car_list = "Marca\tModelo\tColor\tAño\tKM\tFecha de creación\n\n"
        car_list += '\n'.join(
            f"{index}) {car.brand}\t{car.model}\t{car.color}\t{car.year}\t{car.km}\t{car.date_creation}"
        for index, car in enumerate(vehicles))
        return car_list