import sqlite3
import pandas as pd
import bcrypt
import os
import Inserts as ins


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
        clienteID INT,
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

########################################################################################################################
def poblarClientes(data, conexion, cursor):
    ins.insertCliente(data[0],data[2],data[1],data[3],data[4],conexion,cursor)

# empresa (nombre, infoContacto)
def poblarEmpresasDespacho(data, conexion, cursor):
        ins.insertEmpresa(data[4], data[6], conexion, cursor)

# despachadores (nombre, numero_telefono, empresa)
def poblarDespachadores(data, conexion, cursor):
     ins.insertDespachador(data[11],data[12],data[4], conexion, cursor)

# restaurante (nombre)
def poblarRestaurantes(data, conexion, cursor):
     ins.insertRestaurante(data[0], conexion, cursor)

# Local (restaurante, infoContacto, direccion)
def poblarLocales(data, conexion, cursor):
     ins.insertLocal(data[0], data[6], data[5], conexion, cursor)

# plato (nombre, descripcion, disponibilidad, porcion, precio, tiempoPreparacion, nombre_restaurante, lista_ingredientes)
def poblarPlatos(data, conexion, cursor):
    #ins.insertPlato(data[1], data[2], data[3], data[7], data[8], data[9], data[10], data[6], conexion, cursor)
    ins.insertPlato(data[0], data[1], data[2], data[4], data[5], data[6], data[7], data[3], conexion, cursor)

# pedido (clienteCorreo, despachador, fecha, Hora, estado, evaluacionCliente, evaluacionDespachador, platos)
# ['id', 'cliente_x', 'sucursal', 'delivery', 'despachador', 'plato','fecha', 'hora', 'estado', 'pedido', 'resdel', 'cliente_y']
def poblarPedidos(data, conexion, cursor):
    ins.insertPedido(data[1], data[4],data[6],data[7],data[8],data[9],data[10],data[5],conexion, cursor)
    

# Suscripcion (clienteCorreo, empresa, fechaUltimoPago, estado, tipoSuscripcion)
def poblarSuscripciones(data, conexion, cursor):
    print(data[0])
    print(data[1])
    print(data[3])
    print(data[2])
    print(data[5])
    ins.insertSuscripcion(data[0], data[1], data[3], data[2], data[5], conexion, cursor)

########################################################################################################################

conexion = sqlite3.connect('grupo123e2')
cursor = conexion.cursor()
createTables(conexion, cursor)

### PATHS ###
path_empresa_despacho = os.path.join('datos', 'cldeldes.csv')
path_clientes = os.path.join('datos', 'clientes.csv')
path_restaurantes = os.path.join('datos', 'restaurantes.csv')
path_restaurantes2 = os.path.join('datos', 'restaurantes2.csv')
path_pedidos = os.path.join('datos', 'pedidos.csv')
path_pedidos2 = os.path.join('datos', 'pedidos2.csv')
path_comunas = os.path.join('datos', 'comuna.csv')
path_comunas2 = os.path.join('datos', 'comuna2.csv')
path_calificaciones = os.path.join('datos', 'calificacion.csv')
path_suscripciones = os.path.join('datos','suscripciones.csv')
path_platos = os.path.join('datos', 'platos.csv')

#############

#POBLAR CLIENTES 
clientes_datos = pd.read_csv(path_clientes, sep=';', header=0)
clientes_datos = clientes_datos.values.tolist()

for cliente in clientes_datos:
    poblarClientes(cliente, conexion, cursor)
    
#POBLAR EMPRESA 
empresas_datos = pd.read_csv(path_empresa_despacho, sep=';', header=0)
empresas_datos = empresas_datos.values.tolist()

for empresa in empresas_datos:
    poblarEmpresasDespacho(empresa, conexion, cursor)

# POBLAR DESPACHADORES 
for empresa in empresas_datos:
    poblarDespachadores(empresa, conexion, cursor)

# POBLAR RESTAURANTE 
restaurantes_datos = pd.read_csv(path_restaurantes, sep=';', header=0)
restaurantes_datos = restaurantes_datos.values.tolist()

restaurantes_datos2 = pd.read_csv(path_restaurantes2, sep=';', header=0, encoding='latin1')
restaurantes_datos2 = restaurantes_datos2.values.tolist()

for restaurante in restaurantes_datos:
    poblarRestaurantes(restaurante, conexion, cursor)
for restaurante in restaurantes_datos2:
    poblarRestaurantes(restaurante, conexion, cursor)

# POBLAR LOCAL (restaurante, infoContacto, direccion)
for local in restaurantes_datos:
    poblarLocales(restaurante, conexion, cursor)
for local in restaurantes_datos2:
    poblarLocales(restaurante, conexion, cursor)

# POBLAR PLATO (nombre, descripcion, disponibilidad, porciones, precio, tiempoPreparacion, nombre_restaurante, lista_ingredientes)
platos_datos = pd.read_csv(path_platos, sep=';', header=0, usecols= [1,2,3,6,7,8,9,10])
platos_datos = platos_datos.values.tolist()

#pd.read_csv(file_path, usecols=[0, 2])

n = 0
for plato in platos_datos:
    poblarPlatos(plato, conexion, cursor)
    print(f"poblando plato {n}")
    n += 1
#
## POBLAR PEDIDO (clienteCorreo, despachador, fechaHora, estado, evaluacionCliente, evaluacionDespachador, platos)
pedidos_datos = pd.read_csv(path_pedidos, sep=';', encoding='latin1')
pedidos_datos2 = pd.read_csv(path_pedidos2, sep=';',header=0,  encoding='latin1')
evaluaciones_datos=pd.read_csv(path_calificaciones, sep=';', encoding='latin1')

pedidos_combinados = pd.concat([pedidos_datos, pedidos_datos2])
pedidos_finales = pd.merge(pedidos_combinados, evaluaciones_datos, left_on='id', right_on='pedido', how='left')
pedidos_finales = pedidos_finales.values.tolist()
# pedidos finales
# ['id', 'cliente_x', 'sucursal', 'delivery', 'despachador', 'plato','fecha', 'hora', 'estado', 'pedido', 'resdel', 'cliente_y']
for pedido in pedidos_finales:
    poblarPedidos(pedido, conexion, cursor)


## POBLAR SUSCRIPCIONES (correo del Cliente, nombre de la empresa, fecha del proximo pago, estado, tipo de suscripcion)
suscripciones_datos = pd.read_csv(path_suscripciones, sep=';', header=0)
suscripciones_datos = suscripciones_datos.values.tolist()
for suscripcion in suscripciones_datos:
    poblarSuscripciones(suscripcion, conexion, cursor)
# POBLAR SUSCRIPCION (clienteCorreo, empresa, fechaProximaPago, estado, tipoSuscripcion)
