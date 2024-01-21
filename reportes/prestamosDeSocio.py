from tkinter import Tk, Label, Entry, Button, Frame, messagebox, ttk
import sqlite3

def prestamosDeSocio(idSocio):
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT p.* FROM prestamos p, socios s WHERE p.idCliente=s.idCliente and p.idCliente=?'''
    cursor.execute(sql, (idSocio,))

    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return resultado

class VentanaPrestamosDeSocio:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reporte - Prestamos de socio")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Prestamos de socio").grid(column=0, row=0, padx=10, pady=10, sticky="e")

        Label(self.ventana, text="Id de Socio").grid(column=0, row=1, padx=10, pady=10, sticky="e")
        
        self.txt_socio = Entry(self.ventana, width=40)
        self.txt_socio.grid(column=1, row=1, sticky="w")

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
        socio = self.txt_socio.get()
        if not socio:
            messagebox.showerror("Error", "Ingrese el id de un socio a buscar.")
        else:
            datos = prestamosDeSocio(socio)
            for row in self.tree.get_children():
                    self.tree.delete(row)
            for linea in datos:
                self.tree.insert('', 0, values=linea)           
        
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()