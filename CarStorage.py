from models.Car import Car
class CarStorage:
    def __init__(self, filename):
        self.__filename = filename

## Función Lectura -------------------------------------------------------------------
    def read(self): # Lee una linea del archivo
        vehicles = [] # Lista vehiculos 
        filename = self.__filename

        with open(filename) as file:
            #Recorrer lista con datos del archivo
            for line in file.readlines():
                data = line.strip().split()
                car = Car(data[0], data[1], data[2], data[3], data[4]) #Se crea una nueva instancia Auto
                car.date_creation = data[5]
                vehicles.append(car)
        return vehicles
## Función Escritura -------------------------------------------------------------------
    def write(self, car_list): #Escribir los cambios
        filename = self.__filename
        with open(filename, "w") as file:
            file.write(car_list)