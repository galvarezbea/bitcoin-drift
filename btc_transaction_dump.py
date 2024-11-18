# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Análisis de Bitcoin en tiempo real: deriva de lo inmutable
----------------------------------------------------------

Acceso al histórico de transacciones de la cadena de bloques.
Obtiene el número de bloque, el total de transacciones del bloque, su tamaño en bytes y la marca temporal de minado (con fecha, hora, minuto y segundo).
Permite seleccionar el intervalo de bloques a consultar y habilita la descarga a fichero CSV.
"""

# Importa la cadena de conección de btc_connect.py
from btc_connect import btc_connect

import csv, datetime


# Conección al nodo local
rpc_connection = btc_connect()


# Solicita por consola el bloque de transacciones inicial a descargar
#start = 870522
start = int(input("Introduzca el bloque inicial: "))


# Solicita por consola el bloque de transacciones final a descargar. A modo informativo, presenta el último de la cadena de bloques
last_block = rpc_connection.getblockcount()
end = int(input(f"Introduzca el bloque final [último:{last_block}]: "))


# Descarga las transacciones a un fichero CSV
with open("CSV\\btc_transactions.csv", "w", newline="") as csvfile:
    fieldnames = ["Block", "Transactions", "Block size", "Datetime"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (start, end + 1):
        blockhash = rpc_connection.getblockhash(i)
        block = rpc_connection.getblock(blockhash)
        block_time = datetime.datetime.fromtimestamp(block["time"])
        writer.writerow({"Block": i, "Transactions": block["nTx"], "Block size": block["size"], "Datetime": block_time})
