import sqlite3

def insertPersona(nombre, numero_telefono, conexion, cursor):

    cursor.execute(''' 
        INSERT INTO Persona (nombre, numero_telefono) VALUES (?, ?)
    ''', (nombre, numero_telefono,))
    conexion.commit()

def insertCliente(nombre, numero_telefono, correo, clave, direccion, conexion, cursor):
    cursor.execute('''
            SELECT clienteID FROM Cliente WHERE correo = ?
        ''', (correo,))
    resultado = cursor.fetchone()

    if not resultado:
        insertPersona(nombre, numero_telefono, conexion, cursor)
        personaID = cursor.lastrowid

        cursor.execute('''
            INSERT INTO Cliente (clienteID, correo, clave) VALUES (?, ?, ?)
        ''', (personaID, correo, clave,))
        conexion.commit()
    else:
        personaID = resultado[0]

    insertDireccion(personaID, direccion, conexion, cursor)

def insertDireccion(clienteID, direccion, conexion, cursor):

    cursor.execute('''
        INSERT INTO Direccion (clienteID, direccion) VALUES (?, ?)
    ''', (clienteID, direccion,))
    conexion.commit()

def insertEmpresa(nombre, infoContacto, conexion, cursor):

    cursor.execute('''
        INSTERT INTO Empresa (nombre, infoContacto) VALUES (?, ?)
    ''', (nombre, infoContacto))
    conexion.commit()

def insertDespachador(nombre, numero_telefono, empresa, conexion, cursor):

    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    return 0;

def insertRestaurante(nombre, conexion, cursor): 

    cursor.execute(''' 
        INSERT INTO  (nombre) VALUES (?)
    ''', (nombre))
    conexion.commit()

def insertLocal(restaurante, infoContacto, direccion, conexion, cursor):
    cursor.execute('''
            SELECT restauranteID FROM Restaurante WHERE nombre = ?
        ''', (restaurante,))
    restauranteID = cursor.fetchone()[0]

    cursor.execute(''' 
        INSERT INTO Local (restauranteID, infoContacto, direccion) VALUES (?, ?, ?)
    ''', (restauranteID, infoContacto, direccion))
    conexion.commit()

def insertPlato(nombre, descripcion, disponibilidad, tamano, porcion, precio, tiempoPreparacion, restaurante, ingredientes, conexion, cursor):
    cursor.execute('''
            SELECT restauranteID FROM Restaurante WHERE nombre = ?
        ''', (restaurante,))
    restauranteID = cursor.fetchone()[0]

    cursor.execute(''' 
        INSERT INTO Plato (nombre, descripcion, disponibilidad, tamano, porcion, precio, tiempoPreparacion, restauranteID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, descripcion, disponibilidad, tamano, porcion, precio, tiempoPreparacion, restauranteID))
    conexion.commit()

    platoID = cursor.lastrowid
    for ingrediente in ingredientes:
        insertIngrediente(ingrediente, platoID)

def insertIngrediente(nombre, platoID, conexion, cursor):

    cursor.execute(''' 
        INSERT INTO Ingrediente (nombre, platoID) VALUES (?, ?)
    ''', (nombre, platoID))
    conexion.commit()

def insertPedido(clienteCorreo, despachador, fechaHora, estado, evaluacionCliente, evaluacionDespachador, conexion, cursor):
    
    cursor.execute('''
            SELECT clienteID FROM Cliente WHERE correo = ?
        ''', (clienteCorreo,))
    clienteID = cursor.fetchone()[0]

    cursor.execute('''
            SELECT despachadorID FROM Despachador WHERE nombre = ?
        ''', (despachador,))
    despachadorID = cursor.fetchone()[0]

    cursor.execute(''' 
        INSERT INTO Pedido (clienteID, despachadorID, fechaHora, estado, evaluacionCliente, evaluacionDespachador) VALUES (?, ?, ?, ?, ?, ?)
    ''', (clienteID, despachadorID, fechaHora, estado, evaluacionCliente, evaluacionDespachador))
    conexion.commit()

#def insertDetallesPedido(plaotID, cantidad, )