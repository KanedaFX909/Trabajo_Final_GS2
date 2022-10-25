import datetime

print('Sistema de Gestión Autos')
class Auto:
    def __init__(self):
        self.marca = ''
        self.model = ''
        self.color = ''
        self.año = 0
        self.km = 0
        self.fecha_creacion = datetime.date.today()
    
    #Función agregar autos, solicita inputs, solo se aceptan nros en AÑO Y KM
    def agregar_auto(self):
        try:
            self.marca = input('Marca: ')
            self.model = input('Modelo: ')
            self.color = input('Color: ')
            self.año = int(input('Año: '))
            self.km = int(input('km: '))
            return True
        except ValueError:
            print('Ingrese solo numeros en "Año" y "km"')
            return False

    def __str__(self):
        #esta funcion convierte en str todos los elementos de la lista
        return '\t'.join(str(x) for x in [self.marca, self.model, self.color, self.año, self.km, self.fecha_creacion ])

class Inventario:
    #Guardo los autos en esta lista vacia
    def __init__(self):
        self.vehiculos = []
    
    #Llamo a la funcion agregar auto, ingresa a la lista y emite mensaje
    def agregar_auto(self):
        vehiculo = Auto()
        if vehiculo.agregar_auto() == True:
            self.vehiculos.append(vehiculo)
            print ()
            print("El auto se agrego a la lista")
    
    #Funcion para visualizar el inventario       
    def viewInventory(self):
        print('\t'.join(['Nro', 'Marca', 'Modelo','Color', 'Año', 'km','Fecha']))
        for i, vehiculo in enumerate(self.vehiculos) :
            print(i + 1, end='\t')
            print(vehiculo)
#----------------------------------------------------------------------------------------------------

