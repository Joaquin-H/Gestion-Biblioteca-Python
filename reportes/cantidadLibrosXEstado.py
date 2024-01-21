from tkinter import Tk, Label, Entry, Button, Frame, ttk
import sqlite3

def cantidadLibrosXEstado():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT estado, COUNT(*) AS cantidad FROM libros GROUP BY estado''')

    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return resultado

class VentanaCantidadLibrosXEstado:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reporte - Cantidad de libros por estado")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Cantidad de libros por estado:").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        
        self.tree = ttk.Treeview(self.ventana, show='headings', columns=('Estado', 'Cantidad'))
        self.tree.heading('#1', text='Estado')
        self.tree.heading('#2', text='Cantidad')
        self.tree.column('#1', minwidth=50, width=150, anchor="center")
        self.tree.column('#2', minwidth=50, width=100, anchor="center")
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
        datos = cantidadLibrosXEstado()
        for row in self.tree.get_children():
                self.tree.delete(row)
        for linea in datos:
            self.tree.insert('', 0, values=linea)           
        
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()