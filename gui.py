from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database as db


root =Tk()
root.title('Gestion de Inventario')
mainframe=ttk.Frame(root, padding=('3 3 7 10'))
mainframe.grid(row=0, column=0, sticky=(N,S,E,W))

def algo(): #funcion inutil
    if 1==1:
        print('45')
    else: 
        pass
    

class funciones_gui:
    def anadir_inventario(): #ventana donde se estan las opciones para añadir al inventario
        t1=Toplevel(root)
        t1.title('Añadir inventario')
        t1.geometry('450x250+200+5') # valores y creacion del toplevel frame
    
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
        
        ean=StringVar() #definimos funciones stringvar para las variables a manejar
        nombre=StringVar()
        cantidadProducto=StringVar()
        spinbox1=StringVar()
        
        label1=ttk.Label(t1, text='Introduzca los datos:').grid(column=1,row=1,sticky=(W)) #etiquetas de los nombes solicitados
        label2=ttk.Label(t1, text='Introduzca el EAN:').grid(column=1,row=2)
        label3=ttk.Label(t1, text='Introduzca el nombre:').grid(column=1, row=4)
        label4=ttk.Label(t1, text='Introduzca la cantidad: ').grid(column=1,row=6)
    
    
        ean=ttk.Entry(t1, textvariable=ean)
        ean.grid(column=1, row=3, sticky=(E,W), columnspan=2, padx=30) #textos de entrada de infomracion
        nombre=ttk.Entry(t1, textvariable=nombre)
        nombre.grid(column=1, row=5, sticky=(E,W), columnspan=2, padx=30)
        cantidad=ttk.Entry(t1, textvariable=cantidadProducto)
        cantidad.grid(column=1,row=7, sticky=(E,W), columnspan=2, padx=30)
        
        
        def anadido_inventario(): #finaliza la ventana una vez hemos terminado de añadir un producto
            messagebox.showinfo(message='Añadido al inventario', title='Añadido al inventario')
            db.funciones_db.anadir_producto(ean.get(), nombre.get(), cantidad.get())
            db.funciones_db.mostrar_productos()
            t1.destroy()
        
        def trace_callback(*args): #funcion para ver el valor anotado en el campo de cantidad y habilitar el boton para añadir el articulo
            print({cantidadProducto.get()})
            button2=ttk.Button(t1, text='Añadir', command=anadido_inventario, state='default')
            button2.grid(column=1, row=10, pady=10)
    
        cantidadProducto.trace_add("write", trace_callback) #metodo que permite analizar cambios en la entrada de cantidad para lo anteriormnte dicho
        
        button1=ttk.Button(t1, text='Añadir', command=anadido_inventario, state='disable')
        button1.grid(column=1,row=10, pady=10) #boton añadir desactivado
    
    def eliminar_producto():
        """
        This Python function creates a GUI window to input and confirm the deletion of a product by name and
        EAN.
        """
        t2=Toplevel(root)
        t2.title('Eliminar producto')
        t2.geometry('450x300+200+5')
        
        # Configurar las columnas y filas para que se expandan
        t2.grid_columnconfigure(0, weight=1)
        t2.grid_columnconfigure(1, weight=1)
        t2.grid_columnconfigure(2, weight=1)
        t2.grid_rowconfigure(0, weight=1)
        t2.grid_rowconfigure(1, weight=1)
        t2.grid_rowconfigure(2, weight=1)
        t2.grid_rowconfigure(3, weight=1)
        t2.grid_rowconfigure(4, weight=1)
        t2.grid_rowconfigure(5, weight=1)
        t2.grid_rowconfigure(6, weight=1)
        t2.grid_rowconfigure(7, weight=1)
        t2.grid_rowconfigure(8, weight=1)
        t2.grid_rowconfigure(9, weight=1)
        
        nombre=StringVar() #Se definen las variables a manejar 
        ean=StringVar()
        
        def trace_callback(*args): #funcion para ver valores  introducidos en el campo de nombre y habilitar el boton de eliminar al introducir un valor
            print({nombre.get()})
            button1=ttk.Button(t2, text='Eliminar por Nombre', command=eliminar_producto_nombre, state='default')
            button1.grid(column=1, row=5, pady=10)
            
            
        def trace_callback2(*args): #idem, pero para el campo de EAN
            print({ean.get()})
            button2=ttk.Button(t2, text='Eliminar por EAN', command=eliminar_producto_ean, state='default')
            button2.grid(column=2, row=5, pady=10, padx=10, sticky=(W))
        
        
        
        def eliminar_producto_nombre():
            respuesta=messagebox.askyesno(message='¿Está seguro de que desea eliminar el producto?', title='Eliminar producto')
            if respuesta==True:
                messagebox.showinfo(message='Producto eliminado', title='Producto eliminado')
                db.funciones_db.eliminar_producto_nombre(nombre.get())
                db.funciones_db.mostrar_productos()
                t2.destroy()
            else:
                messagebox.showinfo(message='Operación cancelada', title='Operación cancelada')
                t2.destroy()
        def eliminar_producto_ean():
            respuesta=messagebox.askyesno(message='¿Está seguro de que desea eliminar el producto?', title='Eliminar producto')
            if respuesta==True:
                messagebox.showinfo(message='Producto eliminado', title='Producto eliminado')
                db.funciones_db.eliminar_producto_ean(ean.get())
                db.funciones_db.mostrar_productos()
                t2.destroy()
            else:
                messagebox.showinfo(message='Operación cancelada', title='Operación cancelada')
                t2.destroy()
        
        label1=ttk.Label(t2, text='Introduzca el nombre del producto a eliminar:')
        label1.grid(column=1,row=1,sticky=(W))
        label2=ttk.Label(t2, text='Introduzca el EAN del producto a eliminar:')
        label2.grid(column=1,row=3,sticky=(W))
        nombre_entry=ttk.Entry(t2, textvariable=nombre)
        nombre_entry.grid(column=1, row=2, sticky=(E,W), columnspan=2, padx=30)
        ean_entry=ttk.Entry(t2, textvariable=ean)
        ean_entry.grid(column=1, row=4, sticky=(E,W), columnspan=2, padx=30)
        button1=ttk.Button(t2, text='Eliminar por Nombre', command=eliminar_producto_nombre, state='disabled')
        button1.grid(column=1,row=5, pady=10)
        button3=ttk.Button(t2, text='Eliminar por EAN', command=eliminar_producto_ean, state='disabled')
        button3.grid(column=2, row=5, pady=10, padx=10, sticky=(W))
        nombre.trace_add('write', trace_callback) 
        ean.trace_add('write', trace_callback2)
    
    def iniciar_gui():

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

        button1=ttk.Button(mainframe, text='Añadir inventario', command=funciones_gui.anadir_inventario).grid(column=1, row=3)
        button2=ttk.Button(mainframe, text='Mostrar todo el inventario', command=funciones_gui.mostrar_inventario).grid(column=2, row=3)
        button3=ttk.Button(mainframe, text='Elminar un producto', command=funciones_gui.eliminar_producto).grid(column=4, row=3)
        button4=ttk.Button(mainframe, text='Buscar un producto', command=algo).grid(column=5,row=3)
        root.mainloop()

    def mostrar_inventario():
        t3=Toplevel(root)
        t3.title('Mostrar todo el inventario')
        t3.geometry('700x300+200+5')
        
        t3.grid_columnconfigure(0, weight=1)
        t3.grid_columnconfigure(1, weight=1)
        t3.grid_columnconfigure(2, weight=1)
        t3.grid_rowconfigure(0, weight=1)
        t3.grid_rowconfigure(1, weight=1)
        t3.grid_rowconfigure(2, weight=1)
        t3.grid_rowconfigure(3, weight=1)
        t3.grid_rowconfigure(4, weight=1)
        t3.grid_rowconfigure(5, weight=1)
        t3.grid_rowconfigure(6, weight=1)
        t3.grid_rowconfigure(7, weight=1)
        t3.grid_rowconfigure(8, weight=1)
        t3.grid_rowconfigure(9, weight=1)
        
        tree=ttk.Treeview(t3,columns=('EAN', 'Nombre', 'Cantidad'), show='headings')
        tree.heading('EAN', text='EAN')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Cantidad', text='Cantidad')
        tree.grid(column=1, row=1, sticky=(N,S,E,W))
        
        scroll=ttk.Scrollbar(t3, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        scroll.grid(column=2, row=1, sticky=(N,S))
        
        cursor=db.conexion.execute('SELECT * FROM productos1')
        for row in cursor:
            tree.insert('', 'end', values=row)
        
    def buscar_producto():
        t4=Toplevel(root)
        t4.title('Buscar un producto')
        t4.geometry('450x300+200+5')
        
        # Configurar las columnas y filas para que se expandan
        t4.grid_columnconfigure(0, weight=1)
        t4.grid_columnconfigure(1, weight=1)
        t4.grid_columnconfigure(2, weight=1)
        t4.grid_rowconfigure(0, weight=1)
        t4.grid_rowconfigure(1, weight=1)
        t4.grid_rowconfigure(2, weight=1)
        t4.grid_rowconfigure(3, weight=1)
        t4.grid_rowconfigure(4, weight=1)
        t4.grid_rowconfigure(5, weight=1)
        t4.grid_rowconfigure(6, weight=1)
        t4.grid_rowconfigure(7, weight=1)
        t4.grid_rowconfigure(8, weight=1)
        t4.grid_rowconfigure(9, weight=1)
        
funciones_gui.iniciar_gui()
