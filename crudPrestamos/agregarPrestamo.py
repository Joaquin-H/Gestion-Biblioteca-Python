from tkinter import *
import sqlite3
from tkinter import messagebox

def crearPrestamo(socio, libro, fecha, cantDiasDevolucion):
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    sql = '''UPDATE libros SET estado="Prestado" WHERE codigo=?'''
    cursor.execute('''INSERT INTO prestamos (idCliente, codigoLibro, fechaPrestamo, cantDiasDevolucion) VALUES (?, ?, ?, ?)''', (socio, libro, fecha, cantDiasDevolucion))
    cursor.execute(sql, (libro,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Éxito", "Prestamo agregado correctamente.")

class VentanaAgregarPrestamo:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Agregar prestamo")
        self.ventana.geometry("500x250")
        
        Label(self.ventana, text="Id Socio:").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Id Libro:").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Fecha (dd/mm/aaaa):").grid(column=0, row=2, padx=10, pady=10, sticky="e")
        Label(self.ventana, text="Dias para devolucion:").grid(column=0, row=3, padx=10, pady=10, sticky="e")
        
        self.txt_socio = Entry(self.ventana, width=40)
        self.txt_libro = Entry(self.ventana, width=40)
        self.txt_fecha = Entry(self.ventana, width=40)
        self.txt_cantDias = Entry(self.ventana, width=40)
        
        self.txt_socio.grid(column=1, row=0, sticky="w")
        self.txt_libro.grid(column=1, row=1, sticky="w")
        self.txt_fecha.grid(column=1, row=2, sticky="w")
        self.txt_cantDias.grid(column=1, row=3, sticky="w")
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=5, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        socio = self.txt_socio.get()
        libro = self.txt_libro.get()
        fecha = self.txt_fecha.get()
        cantDiasDevolucion = self.txt_cantDias.get()
        crearPrestamo(socio, libro, fecha, cantDiasDevolucion)
        
    def cancelar(self):
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()