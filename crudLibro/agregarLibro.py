from tkinter import *
import sqlite3
from tkinter import messagebox

import sys
sys.path.insert(0, "..\TP Dao")
from entidades.libro import Libro

def crearLibroBD(titulo, precioRep):

    nuevoLibro = Libro(titulo, precioRep, "Disponible")
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES (?, ?, ?)''', (nuevoLibro.titulo, nuevoLibro.precioReposicion, nuevoLibro.estado))
    conn.commit()
    conn.close()
    messagebox.showinfo("Exito", "Libro añadido correctamente.")
    
class VentanaAgregarLibro:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Agregar libro")
        self.ventana.geometry("500x250")
        
        Label(self.ventana, text="Titulo").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Precio reposicion").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        
        self.txt_titulo = Entry(self.ventana, width=40)
        self.txt_precioRep = Entry(self.ventana, width=40)
        
        self.txt_titulo.grid(column=1, row=0, sticky="w")
        self.txt_precioRep.grid(column=1, row=1, sticky="w")
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        
        titulo = self.txt_titulo.get()
        precioRep = int(self.txt_precioRep.get())
        crearLibroBD(titulo, precioRep)
            
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()