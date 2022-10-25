from Autos import Auto
from Autos import Inventario
from datos import Notes

# --------- Menu -----------------------------------------------------------------------
inventory = Inventario() #guardo la clase inventario dentro de una variable (inventory)
while True:
    #Muestro opciones disponibles
    print('1 - Agregar un nuevo Auto')
    print('2 - Borrar Auto')
    print('3 - Visualizar Inventario')
    print('4 - Editar Auto en Inventario')
    print('5 - Exportar Datos')
    print('6 - Salir del Sistema')

    userInput=input('Elija una opción: ') 
    #Agregar 
    if userInput=="1": 
        inventory.agregar_auto()
    #Borrar
    elif userInput=='2':
        if len(inventory.vehiculos) < 1:
            print('No hay vehiculos en el inventario')
            continue
        inventory.viewInventory()
        item = int(input('Ingrese el numero del Auto a borrarse: '))
        if item - 1  > len(inventory.vehiculos):
            print('El numero no existe')
        else:
            inventory.vehiculos.remove(inventory.vehiculos[item - 1])
            print ()
            print('Se quito el auto de la lista exitosamente')
    #Mostrar        
    elif userInput == '3':
        if len(inventory.vehiculos) < 1:
            print('No hay vehiculos en el inventario')
            continue
        inventory.viewInventory()
    #Edit
    elif userInput == '4':
        if len(inventory.vehiculos) < 1:
            print('No hay vehiculos en el inventario')
            continue
        inventory.viewInventory()
        item = int(input('Ingrese el numero del Auto a editar: '))
        if item - 1  > len(inventory.vehiculos):
            print('El numero no existe')
        else:
            automobil = Auto()
            if automobil.agregar_auto() == True :
                inventory.vehiculos.remove(inventory.vehiculos[item - 1])
                inventory.vehiculos.insert(item - 1, automobil)
                print ()
                print('Se actualizo el dato')
    #Exportar txt
    elif userInput == '5':
        if len(inventory.vehiculos) < 1:
            print('No hay vehiculos en el inventario')
            continue
        f = open('inventario.txt', 'w')
        f.write('\t'.join(['Marca', 'Modelo','Color', 'Año', 'km', 'Fecha']))
        f.write('\n')
        for vehiculo in inventory.vehiculos:
            f.write('%s\n' %vehiculo)
        f.close()
        print('Se exporto la lista en archivo txt')
    #Salir
    elif userInput == '6':
        print('Cerrando sistema')
        break
    #Input ivalido
    else:
        print('La opción no es valida, ingrese nuevamente.')

