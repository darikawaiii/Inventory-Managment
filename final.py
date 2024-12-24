'''Proyecto final de gestion de inventario
Creador: Darío Martínez
Correo Electronico: dariopagnanelli@outlook.es'''
import os
#Variables Globales a todas las clases:
articulosLista = []  # Lista que contendrá los diccionarios de los artículos

class producto:
    
    def __init__(self, Nombre,Categoria,Precio,Cantidad): #Definimos el constructor con las categorias del producto
        self.nombre=Nombre
        self.categoria=Categoria
        self.precio=Precio
        self.cantidad=Cantidad
    
    def agregarNuevoProducto():
        limpiar.pantalla()
        veces = int(input("\nIntroduce el número de artículos a ingresar: "))

        for x in range(veces): #Iteramos por  cada producto a ingresar
    # Introducir los detalles del producto
            Nombre = input("\nIntroduce el nombre del producto: ")
            Categoria = input("\nIntroduce la categoría: ")
            IntroducirPrecio=int(input("\nIntroduce el precio: €"))
            if IntroducirPrecio > 0: #Verificacion que el precio es mayor que 0
                Precio=0
                Precio=IntroducirPrecio
            else: #Se reinicia el metodo en caso de que el valor introducido no sea valido 
                input('\nEl precio introducido debe ser mayor a 0. Presione enter')
                limpiar.pantalla()
                producto.agregarNuevoProducto()
                
            IntroducirCantidad= int(input("\nIntroduce la cantidad: "))
            if IntroducirCantidad>=0: #Condicion para que la cantidad no sea un numero negativo
                Cantidad=0
                Cantidad=IntroducirCantidad
            else:#se reinicia en el caso deque no se cumpla la condicion 
                input('\nLa cantidad introducida debe ser mayor o igual a 0. Presione enter')
                verificar=False
                limpiar.pantalla()
                producto.agregarNuevoProducto()
        #Creamos un diccionario para cada articulo que va a ir dentro de una lista
            articuloDiccionario = {'Nombre': Nombre, 'Categoria': Categoria, 'Precio': Precio, 'Cantidad': Cantidad}
    
            articuloDuplicado = False  # Marcador para la condición de si hay articulos duplicados agregarlos o no a la lista
    
        # Verificar si el artículo ya está en la lista
            for y in articulosLista:
        # Comparamos todos los campos para verificar duplicados
                if articuloDiccionario["Nombre"] == y["Nombre"] and articuloDiccionario["Categoria"] == y["Categoria"] and articuloDiccionario["Precio"] == y["Precio"] and articuloDiccionario["Cantidad"] == y["Cantidad"]:
                    print('\nEl artículo ya está presente en la lista.')
                    articuloDuplicado = True  # Marcamos que hay un duplicado
                break  
        
        # Si no es un duplicado, lo agregamos a la lista
            if not articuloDuplicado:
                articulosLista.append(articuloDiccionario)
                print(f'\nEl artículo {articuloDiccionario["Nombre"]} se ha añadido con éxito.')

        # Mostrar los artículos en la lista
        print("\nArtículos en la lista:")
        for articulo in articulosLista:
            print(articulo)
        verificar=False
        return verificar

    def actualizarProducto():
        valorActualizarPrecio=int(input('Desea modificar precio o stock? 1.Modificar Precio 2.Modificar Stock:  '))

        if valorActualizarPrecio==1: #modificar precio 
            nombreValorActualizar=input('Introduzca el nombre del articulo: ')
    
            for diccionario in articulosLista: #Imprime lista por pantalla
                print(diccionario)
    
            precioValorActualizar=int(input("Introduzca el nuevo precio: "))
            if precioValorActualizar>0: #Condicional para revisar precio
                for diccionario in articulosLista:
                    if diccionario['Nombre'] == nombreValorActualizar:
                        diccionario['Precio'] = precioValorActualizar#Actualiza el precio
                    break
            else:
                print('El precio debe ser mayor que 0')
                verificar=False
                return verificar

        elif valorActualizarPrecio==2:#modificar stock
            for diccionario in articulosLista: #Imprime los articulos de la lista
                print(diccionario) 
            nombreValorActualizar=input('Introduzca el nombre del articulo: ') 
            
            cantidadValorActualizar=int(input('Introduzca el nuevo stock: '))
            if cantidadValorActualizar >= 0: #Condicional para validar entrada
                for diccionario in articulosLista:
                    if diccionario['Nombre']==nombreValorActualizar:
                        diccionario['Cantidad']=cantidadValorActualizar #Actualiza el stock del articulo
                    break
            else:
                print('El valor introducido debe ser mayor o igual a 0')
                verificar=False
                return verificar
        
        else: #valor no valido  
            print('El valor introducido no es valido')
            verificar=False
            return verificar
    
    def eliminarProducto():
        valorBuscar=str(input('Introduce nombre del articulo a buscar: ')) 
        valorEliminar=False #Marcador para comprobar si el valor existe en la lista

        for z in articulosLista:
            if z["Nombre"]==valorBuscar: #comparamos el nombre introducido con las claves 'nombre' de la lista de diccionarios
                articulosLista.remove(z) #removemos el diccionario de la lista
                valorEliminar=True
                input("El producto ha sido eliminado. Presione enter para continuar")
                
            if not valorEliminar:#en el caso de que el valor introducido no exista
                input('El valor introducido no existe. Presione enter para continuar.')
                limpiar.pantalla()
                producto.eliminarProducto()

    def buscarProducto():
        valorParaBuscar=str(input('Introduce el nombre del articulo a buscar: '))
        valorBuscarNoError=False #Bandera para el bucle

        for articulo in articulosLista:
            if articulo["Nombre"]==valorParaBuscar: #busca en la iteracion por la clave nombre de cada diccionario
                valorBuscarNoError=True
                print(f'El producto que busca es:')
                print(articulo)
                input('\nPresione enter para continuar...')
                break

        if not valorBuscarNoError: #En caso de que no encuentre la clave, sigue insistiendo
            input('\nEl nombre introducido no existe. Presione enter para continuar...')
            producto.buscarProducto()


class inventario: 
    
    def __init__(self, Nombre,Categoria,Precio,Cantidad): #Definimos el constructor con las categorias del producto
        self.nombre=Nombre
        self.categoria=Categoria
        self.precio=Precio
        self.cantidad=Cantidad

    def main():
        print('\nBienvenido al programa de gestión de inventario')
        print('\n1.Agregar un nuevo producto\n')
        print('2.Actualizar un producto existnte\n')
        print('3.Eliminar un producto existente\n')
        print('4.Mostrar inventario\n')
        print('5.Buscar un producto\n')
        print('6.Salir del programa\n')
        eleccion=int(input('Seleccione una opcion: '))
        return eleccion
    
    def mostrarInventario():
        limpiar.pantalla()
        print("\nArtículos en el inventario:")
        for articulo in articulosLista:  
            print(articulo)             #Mostramos por pantalla todo el inventario
        input('\nPresione enter para continuar...')

class limpiar:  
    def pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

verificar=False
while verificar==False:
    limpiar.pantalla()
    eleccion=inventario.main()
    if eleccion==1:
        producto.agregarNuevoProducto()
    elif eleccion==2:
        producto.actualizarProducto()
    elif eleccion==3:
        producto.eliminarProducto()
    elif eleccion==4:
        inventario.mostrarInventario()
    elif eleccion==5:
        producto.buscarProducto()
    elif eleccion==6:
        exit()
    else:
        verificar=True
        limpiar.pantalla()
        print('\nEl valor no es valido.')
        input('\nPresione enter para cointinuar...')
        
