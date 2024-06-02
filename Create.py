import sqlite3
import pandas as pd

def createTables(conexion, cursor):
    #Cliente
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente (
        clienteID INTEGER PRIMARY KEY,
        numero_telefono INTEGER,
        correo TEXT,
        clave STR
    )''')
    conexion.commit()

def loadClients(conexion, cursor, data):
    for cliente in data:
        num = cliente[2]
        corr = cliente[1]
        psw = cliente[3]
        cursor.execute('''INSERT INTO Cliente (numero_telefono, correo, clave) VALUES (?,?)''', (num, corr, psw))
        conexion.commit()




conexion = sqlite3.connect('Cliente')
cursor = conexion.cursor()
createTables(conexion, cursor)

dataClientes = []

with open('datos\clientes.csv', 'r') as file:
    for line in file:
        try:
            dataClientes.append(line.strip().split(';'))  # Adjust split(',') based on your delimiter
        except Exception as e:
            None

loadClients(conexion, cursor, dataClientes)