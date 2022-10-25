from Autos import Auto
from Autos import Inventario
import datetime

#Persistencia de Datos
class Notes:
    def __init__(self, archivo = "autos.txt"):
        self.archivo = archivo

    def obtener_todo(self):
        vehiculos = []
        with open(self.archivo, 'r') as fp:
            for nota_como_texto in fp:
                n = self.texto_a_nota(nota_como_texto)
                vehiculos.append(n)
        return vehiculos

    def guardar_todo(self, vehiculos):
        with open(self.archivo, 'w') as fp:
            for vehiculo in vehiculos:
                nota_como_texto = self.nota_a_texto(vehiculo)
                fp.write(nota_como_texto)
            print("Guardado en "+ self.archivo)

    def nota_a_texto(self,vehiculo):
        fc = vehiculo.fecha_creacion
        fecha_en_texto = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        return vehiculo + fecha_en_texto + "\n"

    def texto_a_nota(self, texto):
        texto = texto[:-1] # Sacamos el \n final
        nota_como_lista = texto.split(',')
        n = vehiculo (nota_como_lista[0], nota_como_lista[1])
        fecha = nota_como_lista[2].split('-')
        n.fecha_creacion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return n
