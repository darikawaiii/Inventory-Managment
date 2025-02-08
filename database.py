import sqlite3

conn = sqlite3.connect('productos.db')  # inicializa y crea la base de datos si no existe
cursor = conn.cursor()
print('Base de datos iniciada\n')

conn.execute('''CREATE TABLE IF NOT EXISTS productos(
    EAN INT NOT NULL, 
    Nombre TEXT NOT NULL, 
    Cantidad INT NOT NULL
);''')
conn.commit()
conn.close()
print('Tabla creada\n')

def insertar_producto(EAN, Nombre_producto, Cantidad):
    conn.execute("INSERT INTO productos (EAN, Nombre, Cantidad) VALUES (?, ?, ?)", (EAN, Nombre_producto, Cantidad))
    conn.commit()
    conn.close()
    print('Producto insertado\n')

def mostrar_productos():
    cursor = conn.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    for row in productos:
        print(row)
    conn.close()

def menu(eleccion):
    if eleccion == 1:
        EAN = int(input('Introduzca el EAN: '))
        Nombre_producto = input('Introduzca el nombre del producto: ')
        Cantidad = int(input('Introduzca la cantidad: '))
        insertar_producto(EAN, Nombre_producto, Cantidad)
        conn.close()
    elif eleccion == 2:
        mostrar_productos()
        conn.close()
    else:
        print('Opción no válida')

print('1. Insertar productos\n2. Mostrar productos')
print('Seleccione una opción')

eleccion = int(input('Opción: '))
menu(eleccion)

conn.close()




