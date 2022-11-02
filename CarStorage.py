from models.Car import Car
class CarStorage:
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        vehicles = []
        filename = self.__filename

        with open(filename) as file:
            for line in file.readlines():
                data = line.strip().split()
                car = Car(data[0], data[1], data[2], data[3], data[4])
                car.date_creation = data[5]
                vehicles.append(car)
        return vehicles

    def write(self, car_list):
        filename = self.__filename
        with open(filename, "w") as file:
            file.write(car_list)