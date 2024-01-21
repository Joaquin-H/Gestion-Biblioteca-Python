from tkinter import *
import sqlite3
from tkinter import messagebox

import sys
sys.path.insert(0, "..\TP Dao")
from entidades.socio import Socio

def crearSocioBD(nombre, apellido):
    
    nuevoSocio = Socio(nombre, apellido)
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES (?, ?)''', (nuevoSocio.nombre, nuevoSocio.apellido))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Éxito", "Socio agregado correctamente.")

class VentanaAgregarSocio:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Agregar socio")
        self.ventana.geometry("500x250")
        
        Label(self.ventana, text="Nombre").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Apellido").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        
        self.txt_nombre = Entry(self.ventana, width=40)
        self.txt_apellido = Entry(self.ventana, width=40)
        
        self.txt_nombre.grid(column=1, row=0, sticky="w")
        self.txt_apellido.grid(column=1, row=1, sticky="w")
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        
        nombre = self.txt_nombre.get()
        apellido = self.txt_apellido.get()
        crearSocioBD(nombre, apellido)
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()