import sqlite3
import pandas as pd
import bcrypt
import os
import Inserts as ins
#e
def BorrarTablas():
    cursor.execute('''
    DROP TABLE IF EXISTS Persona
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Empresa
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Despachador
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Cliente
    ''')
    conexion.commit()
    
    cursor.execute('''
    DROP TABLE IF EXISTS Direccion
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Restaurante
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Local
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Plato
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Ingrediente
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS Pedido
    ''')
    conexion.commit()

    cursor.execute('''
    DROP TABLE IF EXISTS platoPedido
    ''')
    conexion.commit()
    
    cursor.execute('''
    DROP TABLE IF EXISTS Suscripcion
    ''')
    conexion.commit()
    
    cursor.execute('''
    DROP DATABASE IF EXISTS Cliente
    ''')
    conexion.commit()

def createTables(conexion, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Persona (
        personaID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255),
        numero_telefono VARCHAR(255)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Empresa (
        empresaID INTEGER PRIMARY KEY AUTOINCREMENT,
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
        direccionID INTEGER PRIMARY KEY AUTOINCREMENT,
        clienteID INT,
        direccion VARCHAR(255),
        FOREIGN KEY(clienteID) REFERENCES Cliente(clienteID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Restaurante (
        restauranteID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Local (
        localID INTEGER PRIMARY KEY AUTOINCREMENT,
        restauranteID INT,
        infoContacto VARCHAR(255),
        direccion VARCHAR(255),
        FOREIGN KEY(restauranteID) REFERENCES Restaurante(restauranteID)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Plato (
        platoID INTEGER PRIMARY KEY AUTOINCREMENT,
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
        ingredienteID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255),
        platoID INT,
        FOREIGN KEY(platoID) REFERENCES Plato(platoID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pedido (
        pedidoID INTEGER PRIMARY KEY AUTOINCREMENT,
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
        CREATE TABLE IF NOT EXISTS platoPedido (
        platoPedidoID INTEGER PRIMARY KEY AUTOINCREMENT,
        platoID INT,
        pedidoID INT,
        FOREIGN KEY(platoID) REFERENCES Plato(platoID),
        FOREIGN KEY(pedidoID) REFERENCES Pedido(pedidoID)
    )
    ''')
    conexion.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suscripcion (
        
        empresaID INT,
        fechaProximaPago DATE,
        estado VARCHAR(255),
        tipoSuscripcion VARCHAR(255),
        PRIMARY KEY (empresaID, clienteID),
        FOREIGN KEY(empresaID) REFERENCES Empresa(empresaID),
        FOREIGN KEY(clienteID) REFERENCES Cliente(clienteID)
    )
    ''')
    conexion.commit()

def poblarClientes(data, conexion, cursor):
    ins.insertCliente(data[0],data[2],data[1],data[3],data[4],conexion,cursor)

def poblarEmpresasDespacho(data, conexion, cursor):
        ins.insertEmpresa(data[4], data[6], conexion, cursor)
conexion = sqlite3.connect('grupo123e2')
cursor = conexion.cursor()

createTables(conexion, cursor)

#POBLAR CLIENTES 
path_clientes = os.path.join('datos', 'clientes.csv')
clientes_datos = pd.read_csv(path_clientes, sep=';', header=0)
clientes_datos = clientes_datos.values.tolist()

for cliente in clientes_datos:
    poblarClientes(cliente, conexion, cursor)
    
#POBLAR DESPACHADOR (DELIVERY)
path_empresa_despacho = os.path.join('datos', 'cldeldes.csv')
empresas_datos = pd.read_csv(path_empresa_despacho, sep=';', header=0)
empresas_datos = empresas_datos.values.tolist()

for empresa in empresas_datos:
     if len(empresa)==13:
         poblarEmpresasDespacho(empresa, conexion, cursor)
#for 

# función para agarrar todos los datos cliente
# 