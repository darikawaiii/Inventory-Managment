import sqlite3

conexion = sqlite3.connect('productos1.db')  # inicializa y crea la base de datos si no existe
cursor = conexion.cursor()

class funciones_db:
    def crear_tabla(): #Crea la tabla productos 1 en el caso de que sea la primera vez que se ejecuta el programa y no exista la tabla
        conexion.execute('''CREATE TABLE IF NOT EXISTS productos1(EAN INT, nombre TEXT, precio INT)''')
        conexion.commit()
        print('Tabla creada\n')

    def anadir_producto(ean, nombre, cantidad): #Añade un producto a la tabla productos1
        conexion.execute('''INSERT INTO productos1 VALUES(?,?,?)''', (ean, nombre, cantidad)) 
        conexion.commit()
        print("Producto añadido\n")

    def mostrar_productos(): #Muestra los productos de la tabla productos1
        cursor=conexion.execute("SELECT * FROM productos1")
        for row in cursor:
            print(row)

    def fin_codigo():
        conexion.execute('''DELETE FROM productos1''')#borra los datos de la tabla en fase de pruebas de codigo, eliminar luego 
        conexion.commit()
        conexion.close()#cierra la base de datos
        print('Base de datos cerrada\n')

    def eliminar_producto_ean(ean):#Elimina un producto de la tabla productos1 por ean
            conexion.execute('''DELETE FROM productos1 WHERE LOWER(EAN) = LOWER(?)''', (ean,))
            conexion.commit()
            print("Producto eliminado\n")

    def eliminar_producto_nombre(nombre):#Elimina un producto de la tabla productos1 por nombre
            conexion.execute('''DELETE FROM productos1 WHERE LOWER(nombre)=LOWER(?)''', (nombre,))
            conexion.commit()
            print("Producto eliminado\n")

    def seleccionar_producto():#Selecciona un producto de la tabla productos1
        seleccion=0
        seleccion=int(input("\nQue dato conoce del producto a buscar? 1.EAN 2.Nombre :"))#Selecciona el dato por el que se va a buscar el producto
        if seleccion==1:
            ean=int(input("Introduce el EAN: "))
            cursor=conexion.execute('''SELECT * FROM productos1 WHERE ean LIKE ?''', ('%'+ean+'%'))
            for row in cursor:
                print(row)
        elif seleccion==2:
            nombre=str(input("Introduce el nombre: "))
            cursor=conexion.execute('''SELECT * FROM productos1 WHERE nombre LIKE ?''', ('%'+nombre+'%'))
            for row in cursor: 
                print(row)
        else: 
            print("Introduce un valor válido\n")
            funciones_db.seleccionar_producto()


    
    




