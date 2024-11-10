# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Análisis de Bitcoin en tiempo real: deriva de lo inmutable
----------------------------------------------------------

Análisis de la mempool.
"""

import requests
import time, csv
from datetime import datetime
from bitcoinrpc.authproxy import JSONRPCException
from river import stats


# Importa la cadena de conección de btc_connect.py
from btc_connect import btc_connect

# Conección al nodo local
rpc_connection = btc_connect()


# Inicializa las estadísticas de River
mean = stats.Mean()
var = stats.Var()
min_stat = stats.Min()
max_stat = stats.Max()


print("---------------------------")
print("Transacciones en la mempool")
print("---------------------------")
print("")

# Descarga las estadísticas a un fichero CSV
with open("btc_mempool.csv", "a", newline="") as csvfile:
    fieldnames = ["Datetime", "Mean", "Var", "Min", "Max"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Escribe la cabecera si el archivo está vacío
    csvfile.seek(0, 2) # Final del archivo
    if csvfile.tell() == 0: 
        writer.writeheader()
    
    # Bucle infinito
    while True:
        try:
            # Obtiente la mempool del nodo local
            mempool = rpc_connection.getrawmempool(True)
        except JSONRPCException as e:
            print(f"Error al obtener la mempool del nodo local: {e}")
            mempool = {}
    
        # Itera sobre cada transacción de la mempool y extrae su tamaño (vsize). Comprueba previamente que exista vsize
        transaction_sizes = [transaction.get('vsize') for transaction in mempool.values() if 'vsize' in transaction]
    
        # Recorre transaction_sizes para actualizar las estadísticas    
        #i=0
        for size in transaction_sizes:
            #print(i, size) 
            if size and size > 0:
                mean.update(size)
                var.update(size)
                min_stat.update(size)
                max_stat.update(size)
            #i+=1            
    
        # Imprime las estadísticas
        print(f"Tamaño medio: {mean.get()}")
        print(f"Tamaño varianza: {var.get()}")
        print(f"Tamaño mínimo: {min_stat.get()}")
        print(f"Tamaño máximo: {max_stat.get()}")
        print("-----")
        
        # Escribe en el fichero CSV
        writer.writerow({"Datetime": datetime.now(), "Mean": mean.get(), "Var": var.get(), "Min": min_stat.get(), "Max": max_stat.get()})
        csvfile.flush()
    
        # Tiempo para realizar la siguiente solicitud (10 segundos)
        time.sleep(10)