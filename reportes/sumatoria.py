from tkinter import Tk, Label, Entry, Button, Frame, ttk
import sqlite3

def sumatoriaPrecioRepLibrosExtraviados():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT sum(l.precioReposicion) as sumaTotal FROM libros l where l.estado="Extraviado"''')

    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return resultado

class VentanaSumatoria:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reporte - Sumatoria de precios de reposicion de libros extraviados:")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Sumatoria de precios de reposicion de libros extraviados").grid(column=0, row=0, padx=10, pady=10, sticky="e")

        self.tree = ttk.Treeview(self.ventana, show='headings', columns=('Sumatoria'))
        self.tree.heading('#1', text='Sumatoria')
        self.tree.column('#1', minwidth=50, width=150, anchor="center")
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
        datos = sumatoriaPrecioRepLibrosExtraviados()
        for row in self.tree.get_children():
                self.tree.delete(row)
        for linea in datos:
            self.tree.insert('', 0, values=linea)           
        
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()