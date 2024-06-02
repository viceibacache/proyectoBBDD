import sqlite3
import pandas as pd
import Inserts as ins

def createTables(conexion, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Persona (
        personaID INT PRIMARY KEY,
        nombre VARCHAR(255),
        numero_telefono VARCHAR(255)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Empresa (
        empresaID INT PRIMARY KEY,
        nombre VARCHAR(255),
        infoContacto VARCHAR(255)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Despachador (
        despachadorID INT PRIMARY KEY,
        empresaID INT,
        FOREIGN KEY(despachadorID) REFERENCES Persona(personaID),
        FOREIGN KEY(empresaID) REFERENCES Empresa(empresaID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente (
        clienteID INT PRIMARY KEY,
        correo VARCHAR(255),
        clave VARCHAR(255),
        FOREIGN KEY(clienteID) REFERENCES Persona(personaID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Direccion (
        direccionID INT PRIMARY KEY,
        clienteID INT,
        direccion VARCHAR(255),
        FOREIGN KEY(clienteID) REFERENCES Cliente(clienteID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Restaurante (
        restauranteID INT PRIMARY KEY,
        nombre VARCHAR(255),
        infoContacto VARCHAR(255),
        direccion VARCHAR(255)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Plato (
        platoID INT PRIMARY KEY,
        nombre VARCHAR(255),
        descripcion VARCHAR(255),
        disponibilidad BOOLEAN,
        tamano VARCHAR(255),
        porcion INT,
        precio FLOAT,
        tiempoPreparacion INT,
        restauranteID,
        FOREIGN KEY(restauranteID) REFERENCES Restaurante(restauranteID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ingrediente (
        ingredienteID INT PRIMARY KEY,
        nombre VARCHAR(255),
        platoID INT,
        FOREIGN KEY(platoID) REFERENCES Plato(platoID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pedido (
        pedidoID INT PRIMARY KEY,
        clienteID INT,
        despachadorID INT,
        fechaHora DATETIME,
        estado VARCHAR(255),
        evaluacionCliente INT,
        evaluacionDespachador INT,
        FOREIGN KEY(clienteID) REFERENCES Cliente(clienteID),
        FOREIGN KEY(despachadorID) REFERENCES Cliente(despachadorID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DetallesPedido (
        detallesPedidoID INT PRIMARY KEY,
        empresaID INT,
        platoID INT,
        cantidad INT,
        precioTotal FLOAT,
        restaurante VARCHAR(255),
        FOREIGN KEY(detallesPedidoID) REFERENCES Pedido(pedidoID),
        FOREIGN KEY(platoID) REFERENCES Plato(platoID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suscripcion (
        empresaID INT,
        clienteID INT,
        fechaProximaPago DATE,
        medioPago VARCHAR(255),
        estado VARCHAR(255),
        tipoSuscripcion VARCHAR(255),
        PRIMARY KEY (empresaID, clienteID),
        FOREIGN KEY(empresaID) REFERENCES Empresa(empresaID),
        FOREIGN KEY(clienteID) REFERENCES Cliente(clienteID)
    )
    ''')
    conexion.commit()

conexion = sqlite3.connect('Cliente')
cursor = conexion.cursor()

createTables(conexion, cursor)

clientes_datos = pd.read_csv('datos\clientes.csv').tolist()