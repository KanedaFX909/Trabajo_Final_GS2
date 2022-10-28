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
    print('6 - Mostrar total de autos en inventario')
    print('7 - Salir del Sistema')

    userInput=input('Elija una opción: ') 
    #Agregar cambiar testo y que llame a self.agregar auto
    #agregar inputs
    if userInput=="1":
        try:
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            color = input('Color: ')
            año = int(input('Año: '))
            km = int(input('km: '))
            inventory.agregar_auto(marca,modelo,color,año,km)
        except ValueError:
            print('Ingrese solo numeros en "Año" y "km"')
        
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
            #antes 
            automobil = inventory.vehiculos[item-1]
            if automobil:
                # inventory.vehiculos.remove(inventory.vehiculos[item - 1])
                # inventory.vehiculos.insert(item - 1, automobil)
                print("Elija dato a editar:")
                print("1: Marca")
                print("2: Modelo")
                print("3: Color")
                print("4: Año")
                print("5: km")
                
                opcion = input("Elija opción: ")
                if opcion == "1":
                    automobil.marca = input("Ingrese la nueva Marca: ")
                elif opcion == "2":
                    automobil.modelo = input("Ingrese el nuevo Modelo ")
                elif opcion == "3":
                    automobil.color = input("Ingrese el nuevo Color ")
                elif opcion == "4":
                    automobil.año = input("Ingrese el nuevo Año ")
                elif opcion == "5":
                    automobil.km = input("Ingrese el nuevo KM ")
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
        
    elif userInput == '6':
    #mostrar sumatoria del total item
        len(inventory.vehiculos)
        cantidad = len(inventory.vehiculos)
        print(cantidad)
    
    #Salir
    elif userInput == '7':
        print('Cerrando sistema...')
        break
    #Input invalido
    else:
        print('La opción no es valida, ingrese nuevamente.')

