from tkinter import Tk, Label, Entry, Button, Frame, messagebox, ttk
import sqlite3

def solicitantesLibroXTitulo(titulo):
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT DISTINCT s.nombre, s.apellido FROM prestamos p, libros l, socios s WHERE p.idCliente=s.idCliente and p.codigoLibro=l.codigo and l.titulo=?'''
    cursor.execute(sql, (titulo,))

    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return resultado

class VentanaSolicitantes:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reporte - Solicitantes de libro por titulo")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Solicitantes de libro por titulo").grid(column=0, row=0, padx=10, pady=10, sticky="e")

        Label(self.ventana, text="Titulo").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        
        self.txt_titulo = Entry(self.ventana, width=40)
        self.txt_titulo.grid(column=1, row=1, sticky="w")

        self.tree = ttk.Treeview(self.ventana, show='headings', columns=('Nombre', 'Apellido'))
        self.tree.heading('#1', text='Nombre')
        self.tree.heading('#2', text='Apellido')
        self.tree.column('#1', minwidth=50, width=100, anchor="center")
        self.tree.column('#2', minwidth=50, width=100, anchor="center")
        self.tree.grid(column=1, row=2, sticky="w")
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Traer info")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        titulo = self.txt_titulo.get()
        if not titulo:
            messagebox.showerror("Error", "Ingrese el titulo de un libro a buscar.")
        else:
            datos = solicitantesLibroXTitulo(titulo)
            for row in self.tree.get_children():
                    self.tree.delete(row)
            for linea in datos:
                self.tree.insert('', 0, values=linea)           

    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()