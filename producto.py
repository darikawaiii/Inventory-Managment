class producto:
    
    def __init__(self, nombre,categoria,precio,cantidad): #Definimos el constructor con las categorias del producto
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.cantidad=cantidad
    
    def __str__(self): #funcion que permite que tenga formato la salida de la lista. 
        return f"Nombre: {Nombre}, Categoria: {Categoria}, Precio: {Precio}, Cantidad: {Cantidad}"

#------------------------------------------------------------------------------------------------------

#1.Añadir un producto, meter dentro de una funcion dentro de la clase inventario
#Añadir un producto al inventario
#Introduce datos del producto
articulosLista = []  # Lista que contendrá los diccionarios de los artículos

# Número de artículos a ingresar
veces = int(input("Introduce el número de artículos a ingresar: "))

for x in range(veces):
    # Introducir los detalles del producto
    Nombre = input("Introduce el nombre del producto: ")
    Categoria = input("Introduce la categoría: ")
    IntroducirPrecio=int(input("Introduce el precio: €"))
    if IntroducirPrecio >0:
        Precio=0
        IntroducirPrecio=Precio
    else:
        print('El precio introducido debe ser mayor a 0: ')
    IntroducirCantidad= int(input("Introduce la cantidad: "))
    if IntroducirCantidad>=0:
        Cantidad=0
        IntroducirCantidad=Cantidad
    else:
        print('La cantidad introducida debe ser mayor o igual a 0')
    
    articuloDiccionario = {'Nombre': Nombre, 'Categoria': Categoria, 'Precio': Precio, 'Cantidad': Cantidad}
    
    articuloDuplicado = False  # Reiniciamos la bandera para cada nuevo artículo
    
    # Verificar si el artículo ya está en la lista
    for y in articulosLista:
        # Comparamos todos los campos para verificar duplicados
        if articuloDiccionario["Nombre"] == y["Nombre"] and articuloDiccionario["Categoria"] == y["Categoria"] and articuloDiccionario["Precio"] == y["Precio"] and articuloDiccionario["Cantidad"] == y["Cantidad"]:
            print('El artículo ya está presente en la lista.')
            articuloDuplicado = True  # Marcamos que hay un duplicado
            break  # Salir del bucle si ya está presente
    
    # Si no es un duplicado, lo agregamos a la lista
    if not articuloDuplicado:
        articulosLista.append(articuloDiccionario)
        print(f'El artículo {articuloDiccionario["Nombre"]} se ha añadido con éxito.')

# Mostrar los artículos en la lista
print("\nArtículos en la lista:")
for articulo in articulosLista:
    print(articulo)

#-------------------------------------------------------------------------------------

#2.Actualizar un producto, meter dentro de la clase inventario  


valorActualizarPrecio=int(input('Desea modificar precio o stock? 1.Modificar Precio 2.Modificar Stock:  '))

if valorActualizarPrecio==1: #modificar precio 
    nombreValorActualizar=input('Introduzca el nombre del articulo: ')
    
    for diccionario in articulosLista:
        print(diccionario)
    
    precioValorActualizar=int(input("Introduzca el nuevo precio: "))
    if precioValorActualizar>0:
        for diccionario in articulosLista:
            if diccionario['Nombre'] == nombreValorActualizar:
                diccionario['Precio'] = precioValorActualizar
            break
    else:
        print('El precio debe ser mayor que 0')

elif valorActualizarPrecio==2:#modificar stock
    nombreValorActualizar=input('Introduzca el nombre del articulo: ')
    for diccionario in articulosLista:
        print(diccionario)
    
    cantidadValorActualizar=int(input('Introduzca el nuevo stock: '))
    
    for diccionario in articulosLista:
        if diccionario['Nombre']==nombreValorActualizar:
            diccionario['Cantidad']=cantidadValorActualizar
        break

else:
    print('El valor introducido no es valido')
    

#---------------------------------------------------------------------------------------------

#3.Eliminar un producto


valorBuscar=str(input('Introduce nombre del articulo a buscar: ')) #Introducimos el nombre del articulo
valorEliminar=False #Marcador condicional en el caso de introducir un valor que no esta en la lista

for z in articulosLista:
    if z["Nombre"]==valorBuscar: #comparamos el nombre introducido con las claves 'nombre' de la lista de diccionarios
        articulosLista.remove(z) #removemos el diccionario de la lista
        valorEliminar=True
    if not valorEliminar:#en el caso de que el valor introducido no exista
       print('El valor introducido no existe') 

print("\nArtículos en la lista:")
for articulo in articulosLista:
    print(articulo)

#----------------------------------------------------------------------------------------------------


#4.Listar todos los productos disponibles

print("\nArtículos en el inventario:")
for articulo in articulosLista:  
    print(articulo)             #Mostramos por pantalla todo el inventario

#----------------------------------------------------------------------------------------------------
#5.Buscar un producto por nombre. 

valorParaBuscar=str(input('Introduce el nombre del articulo a buscar: '))
valorBuscarNoError=False

for c in articulosLista:
    if c['Nombre']==valorParaBuscar:
        print(f'El valor que busca es: {c}')
        valorBuscarError=True
    
    if not valorBuscarNoError:
        print('El nombre introducido no existe')
        break

#-----------------------------------------------------------------------------------------------------

