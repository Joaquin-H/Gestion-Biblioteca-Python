import sqlite3
from datetime import date, timedelta, datetime
from tkinter import Tk, Label, Entry, Button, Frame, ttk

def prestamosDemorados():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT p.* FROM prestamos p, libros l WHERE p.codigoLibro=l.codigo and l.estado="Prestado"''')

    resultado = cursor.fetchall()
    demorados = []
    for p in resultado:
        suma = timedelta(days=p[4])
        fecha = datetime.strptime(p[3], "%"+"d/%m/%Y").date() 
        if date.today() > fecha+suma:
            demorados.append(p)

    conn.commit()
    conn.close()

    return demorados

class VentanaDemorados:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reporte - Prestamos demorados")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Prestamos demorados:").grid(column=0, row=0, padx=10, pady=10, sticky="e")

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
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Traer info")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        datos = prestamosDemorados()
        for row in self.tree.get_children():
                self.tree.delete(row)
        for linea in datos:
            self.tree.insert('', 0, values=linea)           
        
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()