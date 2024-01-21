from entidades.libro import Libro
from entidades.prestamo import Prestamo
from entidades.socio import Socio

class Biblioteca:

    def __init__(self):
        self._prestamos = []
        self._libros = []
        self._socios = []

    @property
    #getPrestamos
    def prestamos(self):
        return self._prestamos

    def addPrestamo(self, prestamo):
        if not isinstance(prestamo, Prestamo):
            raise TypeError("prestamo debe ser un prestamo")
        else:
            self._prestamos.append(prestamo)

    @property
    #getLibros
    def libros(self):
        return self._libros

    def addLibro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("libro debe ser un libro")
        else:
            self._libros.append(libro)

    @property
    #getSocios
    def socios(self):
        return self._socios

    def addSocio(self, socio):
        if not isinstance(socio, Socio):
            raise TypeError("socio debe ser un socio")
        else:
            self._socios.append(socio)
