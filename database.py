import sqlite3

conexion = sqlite3.connect('productos1.db')  # inicializa y crea la base de datos si no existe
cursor = conexion.cursor()
print('Base de datos iniciada\n')

def crear_tabla():
    conexion.execute('''CREATE TABLE IF NOT EXISTS productos1(EAN INT, nombre TEXT, precio INT)''')
    conexion.commit()
    print('Tabla creada\n')

EAN=int(input("Introduce el EAN: "))
nombre=str(input("Introduce el nombre: "))
precio=int(input("Introduce el precio: "))

conexion.execute('''INSERT INTO productos1 VALUES(?,?,?)''', (EAN, nombre, precio))
conexion.commit()
cursor=conexion.execute("SELECT * FROM productos1")
for row in cursor:
    print(row)
conexion.execute('''DELETE FROM productos1''')
conexion.commit()
conexion.close()
print('Base de datos cerrada\n')

