import sqlite3

#conexion = sqlite3.connect('productos1.db')  # inicializa y crea la base de datos si no existe
#cursor = conexion.cursor()
#print('\nBase de datos iniciada\n')

def crear_tabla(): #Crea la tabla productos 1 en el caso de que sea la primera vez que se ejecuta el programa y no exista la tabla
    conexion.execute('''CREATE TABLE IF NOT EXISTS productos1(EAN INT, nombre TEXT, precio INT)''')
    conexion.commit()
    print('Tabla creada\n')

def anadir_producto():
    EAN=int(input("Introduce el EAN: "))
    nombre=str(input("Introduce el nombre: "))
    precio=int(input("Introduce el precio: "))
    conexion.execute('''INSERT INTO productos1 VALUES(?,?,?)''', (EAN, nombre, precio))
    conexion.commit()
    print("Producto añadido\n")

def mostrar_productos():
    cursor=conexion.execute("SELECT * FROM productos1")
    for row in cursor:
        print(row)

def fin_codigo():
    conexion.execute('''DELETE FROM productos1''')#borra los datos de la tabla en fase de pruebas de codigo, eliminar luego 
    conexion.commit()
    conexion.close()
    print('Base de datos cerrada\n')

def eliminar_producto():
    seleccion=0
    seleccion=int(input("\nQué dato conoce del producto a eliminar' 1.EAN 2.Nombre. :"))
    if seleccion==1:
        EAN=int(input("Introduce el EAN: "))
        conexion.execute('''DELETE FROM productos1 WHERE EAN=?''', (EAN,))
        conexion.commit()
        print("Producto eliminado\n")
    elif seleccion==2:
        nombre=str(input("Introduce el nombre: "))
        conexion.execute('''DELETE FROM productos1 WHERE nombre=?''', (nombre,))
        conexion.commit()
        print("Producto eliminado\n")
    else: 
        print("Introduce un valor válido\n")
        eliminar_producto()

def seleccionar_producto():
    seleccion=0
    seleccion=int(input("\nQue dato conoce del producto a buscar? 1.EAN 2.Nombre :"))
    if seleccion==1:
        EAN=int(input("Introduce el EAN: "))
        cursor=conexion.execute('''SELECT * FROM productos1 WHERE EAN=?''', (EAN))
        for row in cursor:
            print(row)
    elif seleccion==2:
        nombre=str(input("Introduce el nombre: "))
        cursor=conexion.execute('''SELECT * FROM productos1 WHERE nombre=''', (nombre))
        for row in cursor: 
            print(row)
    else: 
        print("Introduce un valor válido\n")
        seleccionar_producto()


#crear_tabla()
#anadir_producto() 
#eliminar_producto()
#mostrar_productos() 
#fin_codigo()




