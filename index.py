from tkinter import *
from crudSocios.agregarSocio import VentanaAgregarSocio
from crudSocios.consultarSocio import VentanaConsultarSocio
from crudSocios.eliminarSocio import VentanaEliminarSocio
from crudLibro.agregarLibro import VentanaAgregarLibro
from crudLibro.consultarLibros import VentanaConsultarLibro
from crudLibro.eliminarLibro import VentanaEliminarLibro
from crudLibro.libroExtraviado import VentanaLibroExtraviado
from reportes.reportes import VentanaReportes
from crudPrestamos.agregarPrestamo import VentanaAgregarPrestamo
from crudPrestamos.consultarPrestamo import VentanaConsultarPrestamo

class VentanaMain:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Biblioteca")
        self.ventana.geometry("650x650")
        
        botones = Frame(self.ventana)
        botones.pack(padx=10, pady=50, anchor=NW)
        
        botonRegPrestamo = Button(botones, text="Registrar nuevo prestamo", width=20, height=2)
        botonRegPrestamo.pack(side=TOP, padx=10, pady=5, anchor=W)   

        botonConsultarPrestamo = Button(botones, text="Consultar prestamo", width=20, height=2)
        botonConsultarPrestamo.pack(side=TOP, padx=10, pady=5, anchor=W)  
          
        botonRegCliente = Button(botones, text="Registrar socio", width=20, height=2)     
        botonRegCliente.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonConsultarCliente = Button(botones, text="Consultar socio", width=20, height=2)     
        botonConsultarCliente.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonEliminarCliente = Button(botones, text="Eliminar socio", width=20, height=2)     
        botonEliminarCliente.pack(side=TOP, padx=10, pady=5, anchor=W) 
            
        botonRegLibro = Button(botones, text="Registrar libro", width=20, height=2) 
        botonRegLibro.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonConsultarLibro = Button(botones, text="Consultar libro", width=20, height=2) 
        botonConsultarLibro.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonEliminarLibro = Button(botones, text="Eliminar libro", width=20, height=2) 
        botonEliminarLibro.pack(side=TOP, padx=10, pady=5, anchor=W)

        botonLibroExtraviado = Button(botones, text="Libro extraviado", width=20, height=2) 
        botonLibroExtraviado.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonReportes = Button(botones, text="Reportes", width=20, height=2) 
        botonReportes.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonCancelar = Button(text="Salir", width=20, height=2)
        botonCancelar.pack(side=RIGHT, anchor=SE, padx=10, pady=5)
        
        botonRegPrestamo["command"] = self.regPrestamo
        botonConsultarPrestamo["command"] = self.consultarPrestamo
        botonRegCliente["command"] = self.regCliente
        botonConsultarCliente["command"] = self.consultarCliente
        botonEliminarCliente["command"] = self.eliminarCliente
        botonRegLibro["command"] = self.regLibro
        botonConsultarLibro["command"] = self.consultarLibro
        botonEliminarLibro["command"] = self.eliminarLibro
        botonLibroExtraviado["command"] = self.libroExtraviado
        botonReportes["command"] = self.reportes
        botonCancelar["command"] = self.cancelar
        
    def regPrestamo(self):
        nuevaVentana = VentanaAgregarPrestamo()
        nuevaVentana.mostrar()
    
    def consultarPrestamo(self):
        nuevaVentana = VentanaConsultarPrestamo()
        nuevaVentana.mostrar()

    def regCliente(self):
        nuevaVentana = VentanaAgregarSocio()
        nuevaVentana.mostrar()

    def consultarCliente(self):
        nuevaVentana = VentanaConsultarSocio()
        nuevaVentana.mostrar()

    def eliminarCliente(self):
        nuevaVentana = VentanaEliminarSocio()
        nuevaVentana.mostrar()
    
    def regLibro(self):
        nuevaVentana = VentanaAgregarLibro()
        nuevaVentana.mostrar()

    def consultarLibro(self):
        nuevaVentana = VentanaConsultarLibro()
        nuevaVentana.mostrar()

    def eliminarLibro(self):
        nuevaVentana = VentanaEliminarLibro()
        nuevaVentana.mostrar()

    def libroExtraviado(self):
        nuevaVentana = VentanaLibroExtraviado()
        nuevaVentana.mostrar()
    
    def reportes(self):
        nuevaVentana = VentanaReportes()
        nuevaVentana.mostrar()

    def cancelar(self):
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()
        
VentanaMain().mostrar()
