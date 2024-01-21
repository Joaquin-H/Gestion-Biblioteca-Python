class Libro:

    def __init__(self, titulo, precioReposicion, estado, codigo=0):
        self.validarTipos(codigo, titulo, precioReposicion, estado)
        self._codigo = codigo
        self._titulo = titulo
        self._precioReposicion = precioReposicion
        self._estado = estado

    def validarTipos(self, codigo, titulo, precioReposicion, estado):
        if not isinstance(codigo, int):
            raise TypeError("el codigo debe ser un entero")
        if not isinstance(titulo, str):
            raise TypeError("el titulo debe ser un string")
        if not isinstance(precioReposicion, int):
            raise TypeError("el precio debe ser un float")
        if not isinstance(estado, str):
            raise TypeError("el estado debe ser un string")
        elif estado.lower() not in ["disponible", "prestado", "extraviado"]:
            raise ValueError("el estado no es valido")

    @property
    #getCodigo
    def codigo(self):
        return self._codigo

    @codigo.setter
    #setCodigo
    def codigo(self, _nuevoCodigo):
        if isinstance(_nuevoCodigo, int):
            self._codigo = _nuevoCodigo
        else:
            raise ValueError('el parametro no es un entero')

    @property
    #getTitulo
    def titulo(self):
        return self._titulo

    @titulo.setter
    #setTitulo
    def titulo(self, _nuevoTitulo):
        if isinstance(_nuevoTitulo, str):
            self._titulo = _nuevoTitulo
        else:
            raise ValueError('el parametro no es un string')

    @property
    #getPrecioReposicion
    def precioReposicion(self):
        return self._precioReposicion

    @precioReposicion.setter
    #setPrecioReposicion
    def precioReposicion(self, _nuevoPrecioReposicion):
        if isinstance(_nuevoPrecioReposicion, float):
            self._precioReposicion = _nuevoPrecioReposicion
        else:
            raise ValueError('el parametro no es float')

    @property
    #getEstado
    def estado(self):
        return self._estado

    @estado.setter
    #setEstado
    def estado(self, _nuevoEstado):
        if isinstance(_nuevoEstado, str):
            self._estado = _nuevoEstado
        else:
            raise ValueError('el parametro no es string')
