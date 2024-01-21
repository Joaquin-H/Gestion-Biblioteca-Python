from tkinter import Tk, Label, Entry, Button, Frame, ttk
import sqlite3
from tkinter import messagebox

def buscarTodosPrestamos():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT p.* FROM prestamos p''')

    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return resultado

def consultarPrestamoById(idPrestamo):
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    sql = '''SELECT * FROM prestamos WHERE codigoPrestamo=?'''
    cursor.execute(sql, (idPrestamo,))
    
    resultado = cursor.fetchall()
    
    prestamos = []
    for p in resultado:
        prestamos.append(p)
    
    conn.commit()
    conn.close()
    return prestamos

def devolverLibro(idLibro):
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    sql = '''UPDATE libros SET estado="Disponible" WHERE codigo=?'''
    cursor.execute(sql, (idLibro,))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Exito", "Libro actualizado correctamente.")

class VentanaConsultarPrestamo:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Consultar prestamo")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Id prestamo:").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        
        self.txt_idPrestamo = Entry(self.ventana, width=40)
        self.txt_idPrestamo.grid(column=1, row=0, sticky="w")

        self.tree = ttk.Treeview(self.ventana, show='headings', columns=('IdPrestamo', 'IdCliente', 'codigoLibro', 'fechaPrestamo', 'diasDevolucion'))
        self.tree.heading('#1', text='IdPrestamo')
        self.tree.heading('#2', text='IdCliente')
        self.tree.heading('#3', text='codigoLibro')
        self.tree.heading('#4', text='fechaPrestamo')
        self.tree.heading('#5', text='diasDevolucion')
        self.tree.column('#1', minwidth=50, width=75, anchor="center")
        self.tree.column('#2', minwidth=50, width=75, anchor="center")
        self.tree.column('#3', minwidth=50, width=75, anchor="center")
        self.tree.column('#4', minwidth=50, width=100, anchor="center")
        self.tree.column('#5', minwidth=50, width=75, anchor="center")
        self.tree.grid(column=1, row=1, sticky="w")
        
        botonAct = Frame(self.ventana)
        botonAct.grid(column=1, row=3, sticky="e")

        botonActualizar = Button(botonAct, text="Registrar Devolucion")
        botonActualizar.pack(side="right")

        botonActualizar["command"] = self.actualizar

        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right")
        
        botonAceptar = Button(botones, text="Buscar")
        botonAceptar.pack(side="right", padx=10)

        botonBuscarTodos = Button(botones, text="Buscar Todos")
        botonBuscarTodos.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonBuscarTodos["command"] = self.buscarTodos
        botonCancelar["command"] = self.cancelar

    def actualizar(self):
        seleccionado = self.tree.selection()[0]
        valor = self.tree.item(seleccionado, 'values')[2]
        devolverLibro(valor)
    
    def aceptar(self):
        idPrestamo = self.txt_idPrestamo.get()
        if not idPrestamo:
            messagebox.showerror("Error", "Ingrese el codigo de Prestamo a buscar.")
        else:
            datosSocio = consultarPrestamoById(idPrestamo)
            for row in self.tree.get_children():
                self.tree.delete(row)
            for linea in datosSocio:
                self.tree.insert('', 0, values=linea)

    def buscarTodos(self):
        datos = buscarTodosPrestamos()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for linea in datos:
            self.tree.insert('', 0, values=linea)

    def cancelar(self):
        self.ventana.destroy()

    def mostrar(self):
        self.ventana.mainloop()