import gui as interface
import database

print('Bienvenido al programa de gestion de inventario\n')
print('Esto es para propositos de informacion en consola\n')

def main():
    database.funciones_db.crear_tabla()#Crea la tabla productos1
    print('Tabla creada\n')
    print('Iniciando interfaz grafica\n')
    interface.funciones_gui.iniciar_gui()#Inicia la interfaz grafica
    print('Error al iniciar la interfaz grafica\n')
    exit()#Cierra el programa


if __name__ == "__main__": #Solo se ejecuta si el script se ejecuta directamente, no si se importa
    main()  