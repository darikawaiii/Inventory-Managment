from tkinter import *
from tkinter import ttk
from tkinter import messagebox



def algo(): #funcion inutil
    if 1==1:
        print('45')
    else: 
        pass
    

def anadir_inventario(): #ventana donde se estan las opciones para añadir al inventario
    t1=Toplevel(root)
    t1.title('Añadir inventario')
    t1.geometry('350x250+200+5') # valores y creacion del toplevel frame
    
    # Configurar las columnas y filas para que se expandan
    t1.grid_columnconfigure(0, weight=1)
    t1.grid_columnconfigure(1, weight=1)
    t1.grid_columnconfigure(2, weight=1)
    t1.grid_rowconfigure(0, weight=1)
    t1.grid_rowconfigure(1, weight=1)
    t1.grid_rowconfigure(2, weight=1)
    t1.grid_rowconfigure(3, weight=1)
    t1.grid_rowconfigure(4, weight=1)
    t1.grid_rowconfigure(5, weight=1)
    t1.grid_rowconfigure(6, weight=1)
    t1.grid_rowconfigure(7, weight=1)
    t1.grid_rowconfigure(8, weight=1)
    t1.grid_rowconfigure(9, weight=1)
    
    nombreProducto=StringVar() #definimos funciones stringvar para las variables a manejar
    categoriaProducto=StringVar()
    precioProducto=StringVar()
    cantidadProducto=StringVar()
    spinbox1=StringVar()
    
    label1=ttk.Label(t1, text='Introduzca los datos:').grid(column=2,row=1,sticky=(W)) #etiquetas de los nombes solicitados
    label2=ttk.Label(t1, text='Introduzca el nombre:').grid(column=1,row=2)
    label3=ttk.Label(t1, text='Introduzca la categoria:').grid(column=1, row=4)
    label4=ttk.Label(t1, text='Introduzca el precio: ').grid(column=1,row=6)
    label5=ttk.Label(t1, text='Introduzca la cantidad: ').grid(column=1,row=8)
    
    
    nombre=ttk.Entry(t1, textvariable=nombreProducto).grid(column=1, row=3, sticky=(E,W), columnspan=2, padx=30) #textos de entrada de infomracion
    categoria=ttk.Entry(t1, textvariable=categoriaProducto).grid(column=1, row=5, sticky=(E,W), columnspan=2, padx=30)
    precio=ttk.Entry(t1, textvariable=precioProducto).grid(column=1,row=7, sticky=(E,W), columnspan=2, padx=30)
    cantidad=ttk.Spinbox(t1, from_=1.0, to=10.0, textvariable=spinbox1).grid(column=1,row=9,sticky=(E,W), columnspan=2, padx=30)
    
    def anadido_inventario(): #finaliza la ventana una vez hemos terminado de añadir un producto
        messagebox.showinfo(message='Añadido al inventario', title='Añadido al inventario')
        t1.destroy()
    
    def trace_callback(*args): #funcion para ver el valor anotado en el campo de cantidad y habilitar el boton para añadir el articulo
        print({precioProducto.get()})
        button2=ttk.Button(t1, text='Añadir', command=anadido_inventario, state='default').grid(column=1, row=10, pady=10)
    
    precioProducto.trace_add("write", trace_callback) #metodo que permite analizar cambios en la entrada de cantidad para lo anteriormnte dicho
    
    button1=ttk.Button(t1, text='Añadir', command=anadido_inventario, state='disable').grid(column=1,row=10, pady=10) #boton añadir desactivado
    
    






root =Tk()
root.title('Gestion de Inventario')
mainframe=ttk.Frame(root, padding=('3 3 7 10'))
mainframe.grid(row=0, column=0, sticky=(N,S,E,W))
imgobj=PhotoImage(file='/Users/cristina/Desktop/1.png')
img=ttk.Label(mainframe, image=imgobj).grid(column=3, row=0)

# Configurar las columnas y filas para que se expandan
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)
mainframe.grid_columnconfigure(2, weight=1)
mainframe.grid_columnconfigure(3, weight=1)
mainframe.grid_columnconfigure(4, weight=1)
mainframe.grid_columnconfigure(5, weight=1)
mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(1, weight=1)
mainframe.grid_rowconfigure(2, weight=1)
mainframe.grid_rowconfigure(3, weight=1)

label1=StringVar()
label2=StringVar()
label1=ttk.Label(mainframe, text='Bienvenido al programa de gestión de inventario', justify='center').grid(column=3, row=1)
label2=ttk.Label(mainframe, text='Que desea hacer hoy?').grid(column=3, row=2)

button1=StringVar()
button2=StringVar()
button3=StringVar()
button4=StringVar()

button1=ttk.Button(mainframe, text='Añadir inventario', command=anadir_inventario).grid(column=1, row=3)
button2=ttk.Button(mainframe, text='Mostrar todo el inventario', command=algo).grid(column=2, row=3)
button3=ttk.Button(mainframe, text='Elminar un producto', command=algo).grid(column=4, row=3)
button4=ttk.Button(mainframe, text='Buscar un producto', command=algo).grid(column=5,row=3)


root.mainloop()
