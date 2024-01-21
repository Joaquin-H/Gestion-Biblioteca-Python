from tkinter import Tk, Label, Entry, Button, Frame, ttk
import sqlite3
from tkinter import messagebox

def buscarTodosSocios():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT p.* FROM socios p''')

    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return resultado

def consultarSociosBD(idSocio):
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    sql = '''SELECT s.* From socios s WHERE s.idCliente = ?'''
    cursor.execute(sql, (idSocio,))
    
    resultado = cursor.fetchall()
    
    socios = []
    for socio in resultado:
        socios.append(socio)
    
    conn.commit()
    conn.close()
    return socios

class VentanaConsultarSocio:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Consultar socio")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Id de socio").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        
        self.txt_idSocio = Entry(self.ventana, width=40)
        self.txt_idSocio.grid(column=1, row=0, sticky="w")

        self.tree = ttk.Treeview(self.ventana, show='headings', columns=('ID', 'Nombre', 'Apellido'))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Nombre')
        self.tree.heading('#3', text='Appellido')
        self.tree.column('#1', minwidth=50, width=50, anchor="center")
        self.tree.column('#2', minwidth=50, width=100, anchor="center")
        self.tree.column('#3', minwidth=50, width=100, anchor="center")
        self.tree.grid(column=1, row=1, sticky="w")
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right")
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right", padx=10)

        botonBuscarTodos = Button(botones, text="Buscar Todos")
        botonBuscarTodos.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonBuscarTodos["command"] = self.buscarTodos
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        idSocio = self.txt_idSocio.get()
        if not idSocio:
            messagebox.showerror("Error", "Ingrese el codigo de socio a buscar.")
        else:
            datosSocio = consultarSociosBD(idSocio)
            for row in self.tree.get_children():
                self.tree.delete(row)
            for socio in datosSocio:
                self.tree.insert('', 0, values=socio)

    def buscarTodos(self):
        datos = buscarTodosSocios()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for linea in datos:
            self.tree.insert('', 0, values=linea)

    def cancelar(self):
        self.ventana.destroy()

    def mostrar(self):
        self.ventana.mainloop()