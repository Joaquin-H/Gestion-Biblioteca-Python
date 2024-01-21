from datetime import *
import sys
sys.path.insert(0, "..\TP Dao")
from socio import Socio
from libro import Libro

class Prestamo:
    def __init__(self, fecha, cantDiasDevolucion, socio, libro, codigoPrestamo=0):
        self.validarTipos(codigoPrestamo, fecha, cantDiasDevolucion, socio, libro)
        self._codigoPrestamo = codigoPrestamo
        self._fecha = fecha
        self._cantDiasDevolucion = cantDiasDevolucion
        self._socio = socio
        self._libro = libro

    def validarTipos(self, codigoPrestamo, fecha, cantDiasDevolucion, socio, libro):
        if not isinstance(codigoPrestamo, int):
            raise TypeError("codigoPrestamo debe ser un entero")
        if not isinstance(fecha, date):
            raise TypeError("fecha debe ser un date")
        if not isinstance(cantDiasDevolucion, int):
            raise TypeError("cantDiasDevolucion debe ser un entero")
        if not isinstance(socio, Socio):
            raise TypeError("socio debe ser un socio")
        if not isinstance(libro, Libro):
            raise TypeError("libro debe ser un libro")

    @property
    #getCodigoPrestamo
    def codigoPrestamo(self):
        return self._codigoPrestamo

    @codigoPrestamo.setter
    #setCodigoPrestamo
    def codigoPrestamo(self, _nuevoCodigoPrestamo):
        if isinstance(_nuevoCodigoPrestamo, int):
            self._codigoPrestamo = _nuevoCodigoPrestamo
        else:
            raise ValueError('el parametro no es int')

    @property
    #getFecha
    def fecha(self):
        return self._fecha

    @fecha.setter
    #setFecha
    def fecha(self, _nuevoFecha):
        if isinstance(_nuevoFecha, date):
            self._fecha = _nuevoFecha
        else:
            raise ValueError('el parametro no es datetime')

    @property
    #getCantDiasDevolucion
    def cantDiasDevolucion(self):
        return self._cantDiasDevolucion

    @cantDiasDevolucion.setter
    #setCantDiasDevolucion
    def cantDiasDevolucion(self, _nuevoCantDiasDevolucion):
        if isinstance(_nuevoCantDiasDevolucion, int):
            self._cantDiasDevolucion = _nuevoCantDiasDevolucion
        else:
            raise ValueError('el parametro no es entero')

    @property
    #getSocio
    def socio(self):
        return self._socio

    @socio.setter
    #setSocio
    def socio(self, _nuevoSocio):
        if isinstance(_nuevoSocio, Socio):
            self._socio = _nuevoSocio
        else:
            raise ValueError('el parametro no es socio')

    @property
    #getLibro
    def libro(self):
        return self._libro

    @libro.setter
    #setLibro
    def libro(self, _nuevoLibro):
        if isinstance(_nuevoLibro, Libro):
            self._libro = _nuevoLibro
        else:
            raise ValueError('el parametro no es libro')

    def esDemorado(self):
        suma = timedelta(days=self.cantDiasDevolucion)
        if date.today() > self.fecha+suma:
            return True
        else:
            return False


    def esExtraviado(self):
        suma = timedelta(days=self.cantDiasDevolucion+30)
        if date.today() > self.fecha+suma:
            return True
        else:
            return False
