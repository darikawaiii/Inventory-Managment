import sqlite3

conexion = sqlite3.connect('productos1.db')  # inicializa y crea la base de datos si no existe
cursor = conexion.cursor()
print('Base de datos iniciada\n')

conexion.execute('''CREATE TABLE IF NOT EXISTS productos1 EAN INT, nombre TEXT, precio INT''')
conexion.commit()
print('Tabla creada\n')

conexion.close()

