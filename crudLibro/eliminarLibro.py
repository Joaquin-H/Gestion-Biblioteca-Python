from tkinter import *
import sqlite3
from tkinter import messagebox

def eliminarLibroBD(codigo):

    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    sql = ('''DELETE FROM libros WHERE codigo = ?''')
    cursor.execute(sql, (codigo,))
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
    
class VentanaEliminarLibro:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Eliminar libro")
        self.ventana.geometry("500x250")
        
        Label(self.ventana, text="Codigo de libro").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        
        self.txt_codigo = Entry(self.ventana, width=40)
        
        self.txt_codigo.grid(column=1, row=0, sticky="w")

        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        
        codigo = int(self.txt_codigo.get())
        eliminarLibroBD(codigo)
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()