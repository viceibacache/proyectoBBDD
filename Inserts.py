import sqlite3

def insertPersona(nombre, numero_telefono, conexion, cursor):

    cursor.execute(''' 
        INSERT INTO Persona (nombre, numero_telefono) VALUES (?, ?)
    ''', (nombre, numero_telefono))
    conexion.commit()

def insertCliente(nombre, numero_telefono, correo, clave, direccion, conexion, cursor):

    cursor.execute(''' 
        SELECT COUNT(*) FROM Cliente WHERE correo = ?
    ''', (correo,))
    existe = cursor.fetchone()[0]

    if existe != 0:
        insertPersona(nombre, numero_telefono, conexion, cursor)
        personaID = cursor.lastrowid

        cursor.execute('''
            INSTERT INTO Cliente (clienteID, correo, clave) VALUES (?, ?, ?)
        ''', (personaID, correo, clave))
        conexion.commit()

    insertDireccion(personaID, direccion, conexion, cursor)

def insertDireccion(clienteID, direccion, conexion, cursor):

    cursor.execute('''
        INSTERT INTO Direccion (clienteID, direccion) VALUES (?, ?)
    ''', (clienteID, direccion))
    conexion.commit()

def insertEmpresa(nombre, infoContacto, conexion, cursor):

    cursor.execute('''
        INSTERT INTO Empresa (nombre, infoContacto) VALUES (?, ?)
    ''', (nombre, infoContacto))
    conexion.commit()

def insertDespachador(nombre, numero_telefono, empresaID, conexion, cursor):

    insertPersona(nombre, numero_telefono, conexion, cursor)
    despachadorID = cursor.lastrowid

    cursor.execute(''' 
        INSERT INTO Despachador (despachadorID, empresaID) VALUES (?, ?)
    ''', (despachadorID, empresaID))
    conexion.commit()

def insertRestaurante