import sqlite3

conn = sqlite3.connect("./biblioteca.db")
cursor = conn.cursor()

#CREACION DE TABLAS

"""
cursor.execute('''CREATE TABLE IF NOT EXISTS libros
                  (codigo INTEGER PRIMARY KEY,
                   titulo varchar(60),
                   precioReposicion INTEGER,
                   estado varchar(200))
                ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS socios
                  (idCliente INTEGER PRIMARY KEY,
                   nombre varchar(60),
                   apellido varchar(60))
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos
                  (codigoPrestamo INTEGER PRIMARY KEY,
                   idCliente INTEGER,
                   codigoLibro INTEGER,
                   fechaPrestamo date,
                   cantDiasDevolucion INTEGER,
                   FOREIGN KEY (idCliente) REFERENCES socios(idCliente),
                   FOREIGN KEY (codigoLibro) REFERENCES libros(codigo))
               ''')
"""

#INSERCION DE LIBROS

"""
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Un mundo feliz, de Aldous Huxley", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Orgullo y prejuicio, de Jane Austen", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Crimen y castigo, de Fiódor Dostoyevski", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Lolita, de Vladimir Nabokov", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Don Quijote de la Mancha, de Miguel de Cervantes", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("El retrato de Dorian Gray, de Oscar Wilde.", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("El Principito, de Antoine de Saint-Exupéry.", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("El proceso, de Franz Kafka.", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Cumbres borrascosas, de Emily Brontë.", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("La Odisea, de Homero.", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Guerra y paz, de León Tolstói.", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Frankenstein, de Mary W. Shelley. ", 100, "Disponible")''')
cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Los juegos del hambre, de Suzanne Collins.", 100, "Disponible")''')
"""
#cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Frankenstein, de Mary W. Shelley. ", 100, "Extraviado")''')

#INSERCION DE PRESTAMOS

#cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES ("Un mundo , de Aldous Huxley", 100, "Prestado")''')
#cursor.execute('''INSERT INTO prestamos (idCliente, codigoLibro, fechaPrestamo, cantDiasDevolucion) VALUES (2, 15, '8/4/2023', 20)''')

#INSERCION DE CLIENTES

"""
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("CELESTE", "ACUÑA") ''')
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("OSCAR", "AGUERO") ''')
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("VANESA", "AGUILERA") ''')
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("CECILIA", "ALONSO") ''')
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("PABLO", "BEIZA") ''')
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("HORACIO", "DELGADINO") ''')
cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES ("PAULA", "CUFRE") ''')
"""

conn.commit()
conn.close()
