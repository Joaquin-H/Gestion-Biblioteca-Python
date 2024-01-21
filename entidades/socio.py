class Socio:
    
    def __init__(self, nombre, apellido, idCliente=0):
        self._idCliente = idCliente
        self._nombre = nombre
        self._apellido = apellido

    def validarTipos(self, idCliente, nombre, apellido):
        if not isinstance(idCliente, int):
            raise TypeError("idCliente debe ser un entero")
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser un string")
        if not isinstance(apellido, str):
            raise TypeError("apellido debe ser un string")

    @property
    #getIdCliente
    def idCliente(self):
        return self._idCliente

    @idCliente.setter
    #setId
    def idCliente(self, _nuevoId):
        if isinstance(_nuevoId, int):
            self._idCliente = _nuevoId
        else:
            raise ValueError('el parametro no es un int')

    @property
    #getNombre
    def nombre(self):
        return self._nombre

    @nombre.setter
    #setNombre
    def nombre(self, _nuevoNombre):
        if isinstance(_nuevoNombre, str):
            self._nombre = _nuevoNombre
        else:
            raise ValueError('el parametro no es string')

    @property
    #getApellido
    def apellido(self):
        return self._apellido

    @apellido.setter
    #setApellido
    def apellido(self, _nuevoApellido):
        if isinstance(_nuevoApellido, str):
            self._apellido = _nuevoApellido
        else:
            raise ValueError('el parametro no es string')
