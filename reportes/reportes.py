from tkinter import *
from reportes.cantidadLibrosXEstado import VentanaCantidadLibrosXEstado
from reportes.sumatoria import VentanaSumatoria
from reportes.solicitantes import VentanaSolicitantes
from reportes.prestamosDeSocio import VentanaPrestamosDeSocio
from reportes.demorados import VentanaDemorados

class VentanaReportes:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reportes")
        self.ventana.geometry("600x600")
        
        botones = Frame(self.ventana)
        botones.pack(padx=10, pady=50, anchor=NW)
        
        botonLibXEstado = Button(botones, text="Cantidad de libros en cada estado", width=40, height=2)
        botonLibXEstado.pack(side=TOP, padx=10, pady=5, anchor=W)   

        botonSumatoria = Button(botones, text="Sumatoria precio reposicion", width=40, height=2)     
        botonSumatoria.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonSolicitantes = Button(botones, text="Solicitantes de libro", width=40, height=2)     
        botonSolicitantes.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonPrestamosSocio = Button(botones, text="Prestamos de socio", width=40, height=2)     
        botonPrestamosSocio.pack(side=TOP, padx=10, pady=5, anchor=W) 
            
        botonDemorados = Button(botones, text="Prestamos demorados", width=40, height=2) 
        botonDemorados.pack(side=TOP, padx=10, pady=5, anchor=W)

        botonCancelar = Button(botones, text="Salir", width=40, height=2)
        botonCancelar.pack(side=RIGHT, anchor=SE, padx=10, pady=5)

        botonLibXEstado["command"] = self.cantidadLibrosXEstado
        botonSumatoria["command"] = self.sumatoriaPrecioRepLibrosExtraviados
        botonSolicitantes["command"] = self.solicitantesLibroXTitulo
        botonPrestamosSocio["command"] = self.prestamosDeSocio
        botonDemorados["command"] = self.prestamosDemorados
        botonCancelar["command"] = self.volver
        
    def cantidadLibrosXEstado(self):
        nuevaVentana = VentanaCantidadLibrosXEstado()
        nuevaVentana.mostrar()
    
    def sumatoriaPrecioRepLibrosExtraviados(self):
        nuevaVentana = VentanaSumatoria()
        nuevaVentana.mostrar()

    def solicitantesLibroXTitulo(self):
        nuevaVentana = VentanaSolicitantes()
        nuevaVentana.mostrar()

    def prestamosDeSocio(self):
        nuevaVentana = VentanaPrestamosDeSocio()
        nuevaVentana.mostrar()
    
    def prestamosDemorados(self):
        nuevaVentana = VentanaDemorados()
        nuevaVentana.mostrar()

    def volver(self):
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()

