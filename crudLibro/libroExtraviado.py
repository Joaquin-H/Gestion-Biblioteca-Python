from tkinter import *
import sqlite3
from tkinter import messagebox

def libroExtraviadoBD(titulo):

    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()

    sql = '''UPDATE libros SET estado="Extraviado" WHERE titulo=?'''
    cursor.execute(sql, (titulo,))

    conn.commit()
    conn.close()
    messagebox.showinfo("Exito", "Libro actualizado correctamente.")
    
class VentanaLibroExtraviado:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Actualizar libro")
        self.ventana.geometry("500x250")
        
        Label(self.ventana, text="Titulo del libro:").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.txt_titulo = Entry(self.ventana, width=40)
        self.txt_titulo.grid(column=1, row=0, sticky="w")
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Actualizar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        titulo = self.txt_titulo.get()
        libroExtraviadoBD(titulo)
            
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()