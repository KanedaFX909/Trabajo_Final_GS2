import datetime

print('Sistema de Gestión Autos')
class Auto:
    def __init__(self,marca,modelo,color,año,km):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.km = km
        self.fecha_creacion = datetime.date.today()

    def __str__(self):
        #esta funcion convierte en str todos los elementos de la lista
        return '\t'.join(str(x) for x in [self.marca, self.modelo, self.color, self.año, self.km, self.fecha_creacion ])


class Inventario:
    #Guardo los autos en esta lista vacia
    def __init__(self):
        self.vehiculos = []
        with open("inventario.txt", 'r') as fp:
            linea = 0
            for auto_como_texto in fp:
                linea = linea + 1
                if linea > 1:
                    n = self.texto_auto(auto_como_texto)
                    self.vehiculos.append(n)
    
    #Llamo a la funcion agregar auto, ingresa a la lista y emite mensaje
    def agregar_auto(self,marca,modelo,color,año,km):
        vehiculo = Auto(marca,modelo,color,año,km)
        self.vehiculos.append(vehiculo)
        print ()
        print("El auto se agrego a la lista")
    
    #Funcion para visualizar el inventario       
    def viewInventory(self):
        print('\t'.join(['Nro', 'Marca', 'Modelo','Color', 'Año', 'km','Fecha']))
        for i, vehiculo in enumerate(self.vehiculos) :
            print(i + 1, end='\t')
            print(vehiculo)
            
    def texto_auto(self, texto):
        datos = texto.split("\t")
        a = Auto(datos[0],datos[1],datos[2],datos[3],datos[4])
        return a
    
        
#----------------------------------------------------------------------------------------------------

